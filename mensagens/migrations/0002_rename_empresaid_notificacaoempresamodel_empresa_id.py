# Generated by Django 4.2.3 on 2023-08-15 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensagens', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificacaoempresamodel',
            old_name='empresaid',
            new_name='empresa_id',
        ),
    ]