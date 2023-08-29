# Generated by Django 4.2.3 on 2023-08-10 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lotes', '0002_remove_lotemodel_observacao_remove_lotemodel_valor'),
    ]

	
def migrate_to_new_schema(apps, schema_editor):
    Lotemodel = apps.get_model("lotes", "Lotemodel")
    for lotemodel in Lotemodel.objects.all():
        if not lotemodel.localizacao_id:
            lotemodel.localizacao_id = "default_value_here"
            lotemodel.save()
