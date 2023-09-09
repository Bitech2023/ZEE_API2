# Generated by Django 4.2.3 on 2023-09-09 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_userempresamodel_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nivelid',
        ),
        migrations.AddField(
            model_name='user',
            name='nivel',
            field=models.CharField(choices=[('Ceo', 'Ceo'), ('Agente', 'Agente'), ('App', 'App')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
