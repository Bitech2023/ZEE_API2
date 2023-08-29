# Generated by Django 4.2.3 on 2023-08-14 10:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0007_remove_funcionariosmodel_createdat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionariosmodel',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionariosmodel',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='funcionariosmodel',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='funcionariosmodel',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='funcionariosmodel',
            name='nome_da_empresa',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresas.empresamodel'),
        ),
    ]