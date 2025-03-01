# Generated by Django 5.1.6 on 2025-02-18 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ValueSelection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revenue', models.CharField(choices=[('N/A', 'N/A'), ('1-100K', '1-100K'), ('100K-250K', '100K-250K'), ('250K-500K', '250K-500K'), ('500K-1MIO', '500K-1MIO'), ('>1MIO', '>1MIO')], max_length=10)),
                ('revenue_score', models.IntegerField(default=0)),
                ('cost_optimization', models.CharField(choices=[('N/A', 'N/A'), ('1-25K', '1-25K'), ('25K-100K', '25K-100K'), ('100K-250K', '100K-250K'), ('250K-500K', '250K-500K'), ('>500K', '>500K')], max_length=10)),
                ('cost_score', models.IntegerField(default=0)),
                ('experience', models.CharField(choices=[('N/A', 'N/A'), ('Little', 'Little'), ('Moderate', 'Moderate'), ('Medium', 'Medium'), ('High', 'High'), ('Strong', 'Strong')], max_length=10)),
                ('experience_score', models.IntegerField(default=0)),
                ('regulative', models.CharField(choices=[('N/A', 'N/A'), ('Nice to Have', 'Nice to Have'), ('Potential Gap', 'Potential Gap'), ('Potential Penalty', 'Potential Penalty'), ('Must Have (Possible Penalty)', 'Must Have (Possible Penalty)')], max_length=30)),
                ('regulative_score', models.IntegerField(default=0)),
                ('strategy', models.CharField(choices=[('N/A', 'N/A'), ('Little', 'Little'), ('Moderate', 'Moderate'), ('Medium', 'Medium'), ('High', 'High'), ('Strong', 'Strong')], max_length=10)),
                ('strategy_score', models.IntegerField(default=0)),
                ('total_score', models.IntegerField(default=0)),
            ],
        ),
    ]
