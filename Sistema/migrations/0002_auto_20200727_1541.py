# Generated by Django 3.0.7 on 2020-07-27 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='apellido',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
