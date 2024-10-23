# Generated by Django 5.0.4 on 2024-05-24 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sol_app', '0019_alter_solicitacao_nome_equipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='status',
            field=models.CharField(blank=True, choices=[('AB', 'Aberta'), ('EA', 'Em andamento'), ('FI', 'Finalizada'), ('CA', 'Cancelada')], default='AB', max_length=2, null=True),
        ),
    ]
