# Generated by Django 5.0.4 on 2024-04-30 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sol_app', '0007_alter_solicitacao_contato_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='nome_referencia',
            field=models.CharField(max_length=200, verbose_name='Referência'),
        ),
    ]