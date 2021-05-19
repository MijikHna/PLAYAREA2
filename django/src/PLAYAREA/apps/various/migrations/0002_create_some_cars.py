from django.db import migrations

from apps.various.models import Car

def createCars(apps, schema_editor) -> None:
    car1: Car = Car.objects.create(
      name="Car Nr1",
      model="Mercedes"
    )
    car1.save()

    car2: Car = Car.objects.create(
      name="Car Nr2",
      model="BMW"
    )
    car2.save()

    car3: Car = Car.objects.create(
      name="Car Nr3",
      model="Audi"
    )
    car3.save()

class Migration(migrations.Migration):
    dependencies = [
        ('various', '0001_initial')
    ]

    operations = [migrations.RunPython(createCars)]