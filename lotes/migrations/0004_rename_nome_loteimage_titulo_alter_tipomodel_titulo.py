# Generated by Django 4.2.3 on 2023-09-10 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotes', '0003_rename_lote_lotedetalhemodel_loteid_loteimage_loteid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loteimage',
            old_name='nome',
            new_name='titulo',
        ),
        migrations.AlterField(
            model_name='tipomodel',
            name='titulo',
            field=models.CharField(max_length=125),
        ),
    ]