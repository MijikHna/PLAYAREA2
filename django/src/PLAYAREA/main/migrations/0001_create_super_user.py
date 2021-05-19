import os
from django.db import migrations


def create_superuser(apps, schema_editor):
    from django.contrib.auth.models import User

    superuser = User.objects.create_superuser(
        username='admin',
        email='',
        password='admin'
    )

    superuser.save()


class Migration(migrations.Migration):
    dependencies = []

    operations = [migrations.RunPython(create_superuser)]
