# Generated by Django 4.2.3 on 2023-08-11 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotesolicitacaomodel',
            name='finalidade_de_utilizacao',
            field=models.CharField(default='Industrial', max_length=25, verbose_name=([('industrial', 'Industrial'), ('comercial', 'Comercial'), ('logistica e armazenamento', 'Logistica e Armazenamento'), ('tecnologia e inovação', 'Tecnologia e Inovação'), ('turismo e hospitalidade', 'Turismo e Hospitalidade'), ('energia', 'Energia'), ('agricultura e agroindústria', 'Agricultura e Agroindústria'), ('comércio internacional', 'Comércio Internacional'), ('indústria de pesca', 'Indústria de Pesca'), ('desenvolvimento imobiliário', 'Desenvolvimento Imobiliário')],)),
        ),
    ]