# Generated by Django 5.1.6 on 2025-02-19 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('values', '0006_rename_total_score_valueselection_budget_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ValueSelection',
            new_name='ProjectEvaluation',
        ),
    ]
