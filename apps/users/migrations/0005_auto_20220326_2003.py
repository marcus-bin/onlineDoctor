# Generated by Django 3.0 on 2022-03-26 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220326_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.AutoField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
