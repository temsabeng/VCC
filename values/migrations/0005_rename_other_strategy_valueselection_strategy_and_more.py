# Generated by Django 5.1.6 on 2025-02-19 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('values', '0004_rename_strategy_valueselection_other_strategy_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='valueselection',
            old_name='other_strategy',
            new_name='strategy',
        ),
        migrations.RemoveField(
            model_name='valueselection',
            name='category',
        ),
        migrations.RemoveField(
            model_name='valueselection',
            name='score',
        ),
        migrations.AlterField(
            model_name='valueselection',
            name='cost_optimization',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='valueselection',
            name='customer_experience',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='valueselection',
            name='increase_revenue',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='valueselection',
            name='project_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='valueselection',
            name='regulative',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='valueselection',
            name='total_score',
            field=models.IntegerField(default=0),
        ),
    ]
