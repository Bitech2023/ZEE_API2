# Generated by Django 4.2.3 on 2023-08-14 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0021_alter_empresamodel_principais_funcionarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresamodel',
            name='principais_funcionarios',
            field=models.ForeignKey(default=0, max_length=100, on_delete=django.db.models.deletion.CASCADE, to='empresas.funcionariosmodel'),
        ),
    ]
