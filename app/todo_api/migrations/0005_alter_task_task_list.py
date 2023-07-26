# Generated by Django 4.0 on 2023-07-25 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0004_task_task_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo_api.tasklist', to_field='list_uuid'),
        ),
    ]
