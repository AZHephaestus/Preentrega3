# Generated by Django 5.0.1 on 2024-01-14 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GWP', '0002_remove_game_genero_remove_gamegenre_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamegenre',
            name='genero',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]