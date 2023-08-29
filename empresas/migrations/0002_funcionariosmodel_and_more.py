# Generated by Django 4.2.3 on 2023-08-14 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuncionariosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.PositiveSmallIntegerField()),
                ('bi', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='empresamodel',
            name='principais_integrantes',
        ),
        migrations.AddField(
            model_name='empresamodel',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empresamodel',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/lotes/'),
        ),
        migrations.AddField(
            model_name='empresamodel',
            name='principais_funcionarios',
            field=models.ForeignKey(default=1, max_length=100, on_delete=django.db.models.deletion.CASCADE, to='empresas.funcionariosmodel'),
            preserve_default=False,
        ),
    ]
