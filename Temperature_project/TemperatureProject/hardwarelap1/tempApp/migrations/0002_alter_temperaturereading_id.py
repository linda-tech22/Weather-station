# Generated by Django 5.1 on 2024-08-12 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperaturereading',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
