# Generated by Django 5.0.4 on 2024-05-06 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sol_app', '0012_solicitacao_created_by_solicitacao_updated_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitacao',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='solicitacao',
            name='updated_by',
        ),
    ]