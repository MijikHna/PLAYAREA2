from django.db import migrations


def create_testuser(apps, schema_editor):
    from django.contrib.auth.models import User

    user = User.objects.create(
        username='test_user',
        email='',
        password='test_user'
    )

    user.save()


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_create_super_user')
    ]

    operations = [migrations.RunPython(create_testuser)]
