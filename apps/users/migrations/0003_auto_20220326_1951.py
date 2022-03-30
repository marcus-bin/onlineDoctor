# Generated by Django 3.0 on 2022-03-26 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220325_1115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['id'], 'verbose_name': '科室', 'verbose_name_plural': '科室'},
        ),
        migrations.RemoveField(
            model_name='department',
            name='add_time',
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.IntegerField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=30, verbose_name='科室分类名'),
        ),
        migrations.AlterField(
            model_name='department',
            name='parent_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='users.Department', verbose_name='父类目级别'),
        ),
    ]
