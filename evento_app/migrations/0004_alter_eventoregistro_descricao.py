# Generated by Django 5.0.4 on 2024-05-01 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento_app', '0003_alter_eventoregistro_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventoregistro',
            name='descricao',
            field=models.TextField(max_length=200),
        ),
    ]
