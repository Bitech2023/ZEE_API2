# Generated by Django 4.2.3 on 2023-09-10 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lotes', '0006_remove_finalidademodel_tipo_finalidademodel_tipoid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalidademodel',
            name='tipoId',
            field=models.ForeignKey(default='1034e502-7e90-442a-8480-b4443056e4a2', on_delete=django.db.models.deletion.CASCADE, to='lotes.tipolotemodel'),
        ),
    ]
