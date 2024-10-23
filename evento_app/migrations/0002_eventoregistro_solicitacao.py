# Generated by Django 5.0.4 on 2024-04-29 21:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento_app', '0001_initial'),
        ('sol_app', '0007_alter_solicitacao_contato_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventoregistro',
            name='solicitacao',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, to='sol_app.solicitacao'),
            preserve_default=False,
        ),
    ]