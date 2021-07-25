from django.db import models
from django.contrib.auth.models import User

from typing import Dict, Any

from django.db.models.fields.related import ForeignKey
# Create your models here.


class Table(models.Model):
    name = models.CharField(max_length=220)
    modified = models.DateTimeField()
    rows = models.ManyToManyField('Row')
    columns = models.ManyToManyField('Column')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def serialize(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'modified': self.modified,
            'rows': list(map(lambda x: x.serialize(), self.rows.all())),
            'columns': list(map(lambda x: x.serialize(), self.columns.all()))
        }


class Row(models.Model):
    number = models.IntegerField()
    cells = models.ManyToManyField('Cell')

    def __str__(self) -> str:
        return str(self.number)

    def serialize(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'number': self.number,
            'cells': list(map(lambda x: x.serialize(), self.cells.all()))
        }


class Column(models.Model):
    notation = models.CharField(max_length=4)
    cells = models.ManyToManyField('Cell')

    def __str__(self) -> str:
        return self.notation

    def serialize(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'notation': self.notation,
            'cells': list(map(lambda x: x.serialize(), self.cells.all()))
        }


class Cell(models.Model):
    content = models.TextField()
    modified = models.DateTimeField()

    def __str__(self) -> str:
        return self.content

    def serialize(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'content': self.content,
            'modified': self.modified
        }
