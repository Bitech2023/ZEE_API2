# Generated by Django 4.2.3 on 2023-08-29 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lotes', '0028_alter_lotesolicitacaomodel_status_da_solicitacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lotemodel',
            name='localizacao',
        ),
        migrations.AddField(
            model_name='localizacaolotemodel',
            name='loteID',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='lotes.lotemodel'),
        ),
    ]
