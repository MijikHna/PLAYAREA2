# Generated by Django 3.0.5 on 2021-05-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('modified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notation', models.CharField(max_length=4)),
                ('cells', models.ManyToManyField(to='excel_clone.Cell')),
            ],
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('cells', models.ManyToManyField(to='excel_clone.Cell')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('modified', models.DateTimeField()),
                ('columns', models.ManyToManyField(to='excel_clone.Column')),
                ('rows', models.ManyToManyField(to='excel_clone.Row')),
            ],
        ),
    ]