# Generated by Django 4.2.3 on 2023-09-09 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0040_alter_documentosempresamodel_caminho_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresamodel',
            name='telefone',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
