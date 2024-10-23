# Generated by Django 5.0.4 on 2024-05-01 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sol_app', '0008_alter_solicitacao_nome_referencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='data_sol',
            field=models.DateField(verbose_name='Data da Solicitação'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='doc_sol',
            field=models.CharField(max_length=100, verbose_name='Documento da Solicitação'),
        ),
    ]