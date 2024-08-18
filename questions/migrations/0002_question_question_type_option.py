# Generated by Django 5.0.7 on 2024-08-01 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('radio', 'Radio Buttons'), ('scoring', 'Scoring')], default='radio', max_length=10),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='questions.question')),
            ],
        ),
    ]
