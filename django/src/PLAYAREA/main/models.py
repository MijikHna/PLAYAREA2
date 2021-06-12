from django.db import models

from typing import Dict, Any

# Create your models here.


class App(models.Model):
    name = models.CharField(max_length=220)
    name_stringified = models.CharField(
        max_length=220, blank=True, null=True)
    href = models.CharField(max_length=220, blank=True, null=True)
    subApps = models.ManyToManyField('SubApp')

    def __str__(self) -> str:
        return f'{self.name}: {len(self.subApps.all())}'

    def serialize(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'name_stringified': self.name_stringified,
            'href': self.href,
            # 'subApps':  list(map(lambda x: x.serialize(), self.subApps.all())) if self.subApps else self.subApps
            'subApps': list(map(lambda x: x.serialize(), self.subApps.all()))
        }


class SubApp(models.Model):
    name = models.CharField(max_length=220)
    name_stringified = models.CharField(
        max_length=220, blank=True, null=True)
    href = models.CharField(max_length=220)

    def __str__(self) -> str:
        return self.name

    def serialize(self) -> Dict[str, Any]:
        return{
            'id': self.id,
            'name': self.name,
            'name_stringified': self.name_stringified,
            'href': self.href,
        }
