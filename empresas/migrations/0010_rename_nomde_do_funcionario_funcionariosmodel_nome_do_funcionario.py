# Generated by Django 4.2.3 on 2023-08-14 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0009_alter_empresamodel_logo_alter_funcionariosmodel_sexo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionariosmodel',
            old_name='nomde_do_funcionario',
            new_name='nome_do_funcionario',
        ),
    ]
