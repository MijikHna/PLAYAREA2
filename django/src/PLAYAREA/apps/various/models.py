from django.db import models

from typing import Dict
# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=220)
    model = models.CharField(max_length=220)

    def __str__(self) -> str:
        return self.name

    def serialize(self) -> Dict[str, str]:
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model
        }
