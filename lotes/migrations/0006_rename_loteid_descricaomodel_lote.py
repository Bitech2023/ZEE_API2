# Generated by Django 4.2.3 on 2023-08-30 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lotes', '0005_localizacaolotemodel_loteid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='descricaomodel',
            old_name='loteId',
            new_name='lote',
        ),
    ]
