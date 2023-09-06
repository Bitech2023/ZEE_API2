# Generated by Django 4.2.3 on 2023-09-05 14:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0037_remove_empresamodel_dono_delete_donoempresamodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descricaomodel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('descricao', models.CharField(max_length=125)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Finalidademodel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('finalidade', models.CharField(max_length=55)),
                ('descricao', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InfraestruturaModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('informacao', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocalizacaoLoteModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('longitude', models.CharField(max_length=35, null=True)),
                ('latitude', models.CharField(max_length=35, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LoteAtribuicaoModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('data_de_atribuicao', models.DateField(auto_now_add=True)),
                ('valor_da_atribuicao', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('duracao', models.CharField(default='Em meses', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Loteimage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=125)),
                ('imagem', models.ImageField(upload_to='static/imagems/lote/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TipoLote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('tipo', models.CharField(max_length=125)),
                ('descricao', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='pagamento_atribuicao',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('data_do_pagamento', models.DateField(auto_now=True)),
                ('valor_do_pagamento', models.DecimalField(decimal_places=2, max_digits=10)),
                ('numero_de_referencia', models.IntegerField()),
                ('status_do_pagamento', models.CharField(choices=[('pago', 'Pago'), ('pendente', 'Pendente'), ('cancelado', 'cancelado')], default='pendente', max_length=50)),
                ('atribuicao_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotes.loteatribuicaomodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LoteSolicitacaoModel',
            fields=[
                ('data_solicitacao', models.DateField(auto_created=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('status_da_solicitacao', models.CharField(choices=[('em análise', 'Em Análise'), ('rejeitada', 'Rejeitada'), ('aprovada', 'Aprovada')], default='Em Análise', max_length=25)),
                ('finalidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotes.finalidademodel')),
                ('nif_empresa_solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.empresamodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LoteModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('identificadordolote', models.CharField(max_length=125)),
                ('status', models.CharField(choices=[('desocupado', 'Desocupado'), ('ocupado', 'Ocupado'), ('em desenvolvimento', 'Em Deselvovimento')], default='desocupado', max_length=25)),
                ('data_disponibilidade', models.DateField(auto_now_add=True)),
                ('comprimento', models.IntegerField(default=0)),
                ('largura', models.IntegerField(default=0)),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('imagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotes.loteimage')),
                ('localicacaolote', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lotes.localizacaolotemodel')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotes.tipolote')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LoteEmpresaModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('empresaid', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='empresas.empresamodel')),
                ('loteId', models.ManyToManyField(default=True, to='lotes.lotemodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='loteatribuicaomodel',
            name='id_solicitacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lotes.lotesolicitacaomodel'),
        ),
        migrations.AddField(
            model_name='loteatribuicaomodel',
            name='nif_empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.empresamodel'),
        ),
        migrations.AddField(
            model_name='loteatribuicaomodel',
            name='numero_lote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotes.lotemodel'),
        ),
        migrations.CreateModel(
            name='HistoricoLoteModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('descricao', models.TextField()),
                ('data_atribuicao', models.DateField()),
                ('data_saida', models.DateField()),
                ('nif_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.empresamodel')),
                ('numero_lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotes.lotemodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DetalhesModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('detalhes', models.TextField()),
                ('descricao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotes.descricaomodel')),
                ('lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descricoes', to='lotes.lotemodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
