# Generated by Django 4.2.3 on 2023-08-18 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lotes', '0022_historicolotemodel_createdat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicolotemodel',
            old_name='id_empresa',
            new_name='nif_empresa',
        ),
        migrations.RenameField(
            model_name='historicolotemodel',
            old_name='id_lote',
            new_name='numero_lote',
        ),
        migrations.RenameField(
            model_name='loteatribuicaomodel',
            old_name='id_empresa',
            new_name='nif_empresa',
        ),
        migrations.RenameField(
            model_name='loteatribuicaomodel',
            old_name='id_lote',
            new_name='numero_lote',
        ),
        migrations.RenameField(
            model_name='lotesolicitacaomodel',
            old_name='id_empresa_solicitante',
            new_name='nif_empresa_solicitante',
        ),
    ]
