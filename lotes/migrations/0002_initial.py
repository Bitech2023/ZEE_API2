# Generated by Django 4.2.3 on 2023-11-16 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lotes', '0001_initial'),
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lotesolicitacaomodel',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario'),
        ),
        migrations.AddField(
            model_name='loteimage',
            name='lote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotes.lotemodel'),
        ),
        migrations.AddField(
            model_name='loteempresamodel',
            name='empresaId',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='empresas.empresamodel'),
        ),
        migrations.AddField(
            model_name='lotedetalhemodel',
            name='descricao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotes.lotedescricaomodel'),
        ),
        migrations.AddField(
            model_name='lotedetalhemodel',
            name='loteid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotes.lotemodel'),
        ),
        migrations.AddField(
            model_name='loteatribuicaomodel',
            name='id_solicitacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lotes.lotesolicitacaomodel'),
        ),
        migrations.AddField(
            model_name='localizacaolotemodel',
            name='lote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lotes.lotemodel'),
        ),
        migrations.AddField(
            model_name='localizacaoempresamodel',
            name='EmpresaModel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='empresas.empresamodel'),
        ),
        migrations.AddField(
            model_name='historicolotemodel',
            name='idEmpresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.empresamodel'),
        ),
        migrations.AddField(
            model_name='historicolotemodel',
            name='loteId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotes.lotemodel'),
        ),
        migrations.AddField(
            model_name='geolocalizacaomodel',
            name='lote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lotes.lotemodel'),
        ),
        migrations.AddField(
            model_name='finalidadesolicitacaomodel',
            name='solicitacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotes.lotesolicitacaomodel'),
        ),
        migrations.AddField(
            model_name='finalidadesolicitacaomodel',
            name='tipoId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotes.tipolotemodel'),
        ),
        migrations.AddField(
            model_name='documentolotemodel',
            name='loteId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotes.lotemodel'),
        ),
        migrations.AddField(
            model_name='documentolotemodel',
            name='titulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotes.documentotitulomodel'),
        ),
    ]
