# Generated by Django 3.1.6 on 2021-02-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]