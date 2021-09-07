from .models import Table, Row, Column, Cell

import json
from datetime import datetime

from django.contrib.auth.models import User

from django.http.response import JsonResponse, Http404
from django.shortcuts import redirect, render
from django.urls import reverse


from typing import Dict, List, Any

from main.models import App
from playarea.utils.Helper import Helper


app_name: str = "Excel Clone"
# Create your views here.


def new_table(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            req_data: Dict(str, str) = json.loads(request.body.decode('utf-8'))

            table_name = req_data['tableName']

            modifiedTime: datetime = datetime.now()

            # create table
            table: Table = Table.objects.create(
                name=table_name,
                modified=modifiedTime,
                user=request.user
            )

            # create rows
            for i in range(1, 11):
                row: Row = table.row_set.create(
                    number=i,
                )

            # create columns
            for i in range(0, 10):
                column: Column = table.column_set.create(
                    notation=chr(ord('A') + i),
                )

            rows: List[Row] = table.row_set.all()
            columns: List[Column] = table.column_set.all()

            for row in rows:
                for column in columns:
                    cell: Cell = table.cell_set.create(
                        content=f'{row.number}{column.notation}',
                        modified=modifiedTime,
                        row=row,
                        column=column
                    )

                    column.cell_set.add(cell)
                    row.cell_set.add(cell)

            context: Dict[str, Any] = {'tableId': table.id}

            return JsonResponse(data=context, safe=False, status=201)
        else:
            return JsonResponse({'status': 405, 'message': 'Method Not Allowed'}, status=405)
    else:
        return JsonResponse({'status': 401, 'message': 'Unauthorized'}, status=401)


def get_tables(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            tables: List[Table] = Table.objects.filter(user=request.user.id)
            tables_serialized = [
                {'tableName': table.name, 'id': table.id} for table in tables
            ]
            return JsonResponse(tables_serialized, safe=False, status=200)
        else:
            return JsonResponse({'status': 405, 'message': 'Method Not Allowed'}, status=405)
    else:
        return JsonResponse({'status': 401, 'message': 'Unauthorized'}, status=401)


def open_table(request, id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            context: Dict[str, Any] = {
                'title': app_name,
                'js': {
                    'apps': json.dumps(Helper.getAllApps(serialized=True))
                }
            }

            id = id if id else request.GET.get('id')

            if id:
                try:
                    table: Table = Table.objects.get(id=id)
                except Table.DoesNotExist:
                    raise Http404(f'Table with id {id} does not exist')

                context['js']['table'] = json.dumps(
                    table.serialize(), default=str)

            return render(request, 'excel-clone.html', context)
    else:
        return redirect(reverse('login'))


def save_table(request, id):
    if not request.user.is_authenticated:
        return JsonResponse({'status': 401, 'message': 'Unauthorized'}, status=401)

    if request.method != 'PUT':
        return JsonResponse({'status': 405, 'message': 'Method Not Allowed'}, status=405)

    req_data: Dict(str, Any) = json.loads(request.body.decode('utf-8'))

    for cell in req_data['cells']:
        Cell.objects.filter(id=cell['id']).update(content=cell['content'])

    return JsonResponse({'status': 201, 'message': 'Table saved'}, status=201)


def delete_table(request, id):
    pass


def close_table(request, id):
    pass
