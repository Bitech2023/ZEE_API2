# Generated by Django 4.2.3 on 2023-09-05 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lotes', '0004_alter_loteempresamodel_loteid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lotemodel',
            old_name='localicacao',
            new_name='localizacao',
        ),
    ]
