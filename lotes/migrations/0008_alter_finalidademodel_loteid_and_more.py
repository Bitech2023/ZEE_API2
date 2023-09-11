# Generated by Django 4.2.3 on 2023-09-10 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lotes', '0007_alter_finalidademodel_tipoid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalidademodel',
            name='loteid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotes.lotemodel'),
        ),
        migrations.AlterField(
            model_name='finalidademodel',
            name='tipoId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotes.tipolotemodel'),
        ),
    ]
