from django.db import models
from django.contrib.auth.models import User

from typing import Dict, Any

# Create your models here.


class Table(models.Model):
    name = models.CharField(max_length=220, unique=True)
    modified = models.DateTimeField()

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=True
    )

    def __str__(self) -> str:
        return self.name

    def serialize(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'modified': self.modified,
            'rows': list(map(lambda x: x.serialize(), self.row_set.all())),
            'columns': list(map(lambda x: x.serialize(), self.column_set.all())),
            'cells': list(map(lambda x: x.serialize(), self.cell_set.all().order_by('row', 'column')))
        }


class Row(models.Model):
    number = models.IntegerField()
    table = models.ForeignKey(
        Table,
        null=False,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return str(self.number)

    def serialize(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'number': self.number,
            'table': self.table.id,
            'cells': list(map(lambda x: x.serialize(), self.cell_set.all().order_by('row', 'column')))
        }


class Column(models.Model):
    notation = models.CharField(max_length=4)
    table = models.ForeignKey(
        Table,
        null=False,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.notation

    def serialize(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'notation': self.notation,
            'table': self.table.id,
            'cells': list(map(lambda x: x.serialize(), self.cell_set.all().order_by('row', 'column')))
        }


class Cell(models.Model):
    content = models.TextField()
    modified = models.DateTimeField()
    table = models.ForeignKey(
        Table,
        null=False,
        on_delete=models.CASCADE
    )
    row = models.ForeignKey(
        Row,
        null=False,
        on_delete=models.CASCADE
    )
    column = models.ForeignKey(
        Column,
        null=False,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.content

    def serialize(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'content': self.content,
            'modified': self.modified
        }
