# Generated by Django 4.2.3 on 2023-08-14 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0023_alter_empresamodel_principais_funcionarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresamodel',
            name='localizacao_actual',
        ),
    ]
