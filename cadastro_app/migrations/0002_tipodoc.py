# Generated by Django 5.0.4 on 2024-04-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipodoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=3)),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
            ],
        ),
    ]
