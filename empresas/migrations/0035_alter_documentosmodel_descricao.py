# Generated by Django 4.2.3 on 2023-09-04 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0034_documentosmodel_documentosempresamodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentosmodel',
            name='descricao',
            field=models.CharField(max_length=55),
        ),
    ]
