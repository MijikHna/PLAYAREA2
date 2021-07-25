from .models import Table, Row, Column, Cell

import json
from datetime import datetime

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
    if request.user_is_authenticated:
        if request.method == 'POST':
            req_data: Dict(str, str) = json.loads(request.body.decode('utf-8'))

            table_name = req_data['tableName']

            table: Table = Table.objects.create(
                name=table_name,
                modified=datetime.now(),
                user=request.user
            )

            cells: List[Cell] = []
            for i in range(10):
                row: Row = Row.objects.create(
                    number=j,
                    table=table,
                )
                row_cells: List[Cell] = []
                for j in range(10):
                    column: Column = Column.object.get(pk=chr(ord('A') + i))
                    if column is None:
                        column = Column.objects.create(
                            notation=chr(ord('A') + i),
                            table=table
                        )
                    cell: Cell = Cell.objects.create(
                        content='',
                        modified=datetime.now(),
                        row=row,
                        column=column
                    )

                    row_cells.append(cell)

                    column.cells.add(cell)
                    column.save()

                    table.columns.add(column)
                    table.save()

                cells.append(row_cells)

                row.cells.add(row_cells)
                row.save()

                table.rows.add(row)
                table.save()

                # serialize table

            return JsonResponse()

        else:
            return JsonResponse({'status': 401, 'message': 'Bad Request'}, status=400)

    else:
        return JsonResponse({'status': 403, 'message': 'Bad Request'}, status=403)


def open_table(request, id):
    pass


def save_table(request, id):
    pass


def delete_table(request, id):
    pass


def close_table(request, id):
    pass
