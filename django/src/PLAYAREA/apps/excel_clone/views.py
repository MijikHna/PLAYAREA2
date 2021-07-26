from .models import Table, Row, Column, Cell

import json
from datetime import datetime

from django.contrib.auth.models import User

from django.http.response import JsonResponse
from django.shortcuts import render

from typing import Dict, List, Any

from main.models import App
from playarea.utils.Helper import Helper


# Create your views here.


def excel_clone(request):
    if request.user.is_authenticated:
        context: Dict[str, Any] = {
            'title': 'Excel Clone',
            'apps': Helper.getAllApps()
        }

        return render(request, 'excel-clone.html', context)
    else:
        # TODO: return 401/403
        pass


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

            # columns.save()
            # rows.save()
            table_serialized = table.serialize()

            return JsonResponse(table_serialized, safe=False, status=201)

        else:
            return JsonResponse({'status': 401, 'message': 'Bad Request'}, status=400)

    else:
        return JsonResponse({'status': 403, 'message': 'Bad Request'}, status=403)


def get_tables(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            tables: List[Table] = Table.objects.filter(user=request.user.id)
            tables_serialized = [
                {'tableName': table.name, 'id': table.id} for table in tables
            ]
            return JsonResponse(tables_serialized, safe=False, status=200)
        else:
            return JsonResponse({'status': 401, 'message': 'Bad Request'}, status=400)
    else:
        return JsonResponse({'status': 403, 'message': 'Bad Request'}, status=403)


def open_table(request, id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            table: Table = Table.objects.get(id=id)

            return JsonResponse(table.serialize(), safe=False, status=200)
        else:
            return JsonResponse({'status': 401, 'message': 'Bad Request'}, status=400)
    else:
        return JsonResponse({'status': 403, 'message': 'Bad Request'}, status=403)


def save_table(request, id):
    pass


def delete_table(request, id):
    pass


def close_table(request, id):
    pass
