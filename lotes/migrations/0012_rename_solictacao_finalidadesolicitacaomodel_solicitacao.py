# Generated by Django 4.2.3 on 2023-09-10 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lotes', '0011_remove_lotesolicitacaomodel_finalidade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finalidadesolicitacaomodel',
            old_name='solictacao',
            new_name='solicitacao',
        ),
    ]
