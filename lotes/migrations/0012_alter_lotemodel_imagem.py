# Generated by Django 4.2.3 on 2023-09-06 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotes', '0011_alter_lotemodel_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotemodel',
            name='imagem',
            field=models.ImageField(null=True, upload_to='static/imagens/lotes/'),
        ),
    ]
