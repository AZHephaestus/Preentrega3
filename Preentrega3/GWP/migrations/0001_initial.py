# Generated by Django 5.0.1 on 2024-01-14 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='gamegenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('genero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='GWP.game')),
            ],
        ),
    ]
