from empresas.serializers import EmpresaSerializer
from .models import *
from rest_framework import serializers
from rest_framework.response import Response

class TipoLoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLote
        fields = '__all__'

class DescricaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Descricaomodel
        fields = "__all__"
class LoteEmpresaSerializerMany( serializers.ModelSerializer):
    empresa = EmpresaSerializer(read_only=True)
    class Meta:
        model = LoteEmpresaModel
        fields = "__all__"        

class LoteSerializer(serializers.ModelSerializer):
    # localizacao = LocalizacaoLoteSerializer()
    # tipolote = TipoLoteSerializer()
    # estabelecimento = serializers.SerializerMethodField()
    class Meta:
        model = LoteModel
        fields = "__all__"
    # def get_estabelecimento(self, obj):
    #     empresaObj = LoteEmpresaModel.objects.filter(loteId=obj)
    #     # print(empresaObj)
    #     # print(    )
    #     return LoteEmpresaSerializerMany(empresaObj, many=True).data
    
    # def create(self, validated_data):
    #     tipolote_data = validated_data.pop('tipolote')
    #     # localizacao_data = validated_data.pop('localizacao')

    #     tipolote, created = TipoLote.objects.get_or_create(**tipolote_data)
    #     # localizacao, created = LocalizacaoLoteModel.objects.get_or_create(**localizacao_data)

    #     lote = LoteModel.objects.create(tipolote=tipolote, **validated_data)
    #     return lote
class LoteEmpresaSerializer( serializers.ModelSerializer):
    empresa = EmpresaSerializer(read_only=True)
    lote = LoteSerializer(read_only=True)
    class Meta:
        model = LoteEmpresaModel
        fields = "__all__"        

class LocalizacaoLoteSerializer(serializers.ModelSerializer):
    lote = LoteSerializer()
    estabelecimento = serializers.SerializerMethodField()
    class Meta:
        model = LocalizacaoLoteModel
        fields = "__all__"
    def get_estabelecimento(self, obj):
        
        return []
    def create(self, validated_data):
        # tipolote_data = validated_data.pop('tipolote')
        lote_data = validated_data.pop('lote')

        # tipolote, created = TipoLote.objects.get_or_create(**tipolote_data)
        lote, created = LoteModel.objects.get_or_create(**lote_data)

        lote = LocalizacaoLoteModel.objects.create(lote=lote, **validated_data)
        return lote

    def update(self, instance, validated_data):
        lote_data = validated_data.pop('lote')
        
        instance.lote.identificadordolote = lote_data.get('identificadordolote', instance.lote.identificadordolote)
        instance.lote.status = lote_data.get('status', instance.lote.status)
        instance.lote.tipolote_id = lote_data.get('tipolote', instance.lote.tipolote_id)
        instance.lote.comprimento = lote_data.get('comprimento', instance.lote.comprimento)
        instance.lote.largura = lote_data.get('largura', instance.lote.largura)
        instance.lote.imagem = lote_data.get('imagem', instance.lote.imagem)
        instance.lote.valor = lote_data.get('valor', instance.lote.valor)
        instance.lote.descricaolote = lote_data.get('descricaolote', instance.lote.descricaolote)

        instance.lote.save()

        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)

        instance.save()

        return instance
# class LocalizacaoEmpresaSerializer(serializers.ModelSerializer):
#     # empresa = empresaSerializer()
#     estabelecimento = serializers.SerializerMethodField()
#     class Meta:
#         model = LocalizacaoEmpresaModel
#         fields = "__all__"
#     def get_estabelecimento(self, obj):
#         estabelecimentoObj = serializers.SerializerMethodField()
#         return EmpresaSerializer(estabelecimentoObj, many=True)
#     def create(self, validated_data):
#         # tipoempresa_data = validated_data.pop('tipoempresa')
#         empresa_data = validated_data.pop('empresa')

#         # tipoempresa, created = Tipoempresa.objects.get_or_create(**tipoempresa_data)
#         empresa, created = LocalizacaoEmpresaModel.objects.get_or_create(**empresa_data)

#         empresa = LocalizacaoEmpresaModel.objects.create(empresa=empresa, **validated_data)
#         return empresa

#     def update(self, instance, validated_data):
#         empresa_data = validated_data.pop('empresa')
        
#         instance.empresa.identificadordoempresa = empresa_data.get('identificadordoempresa', instance.empresa.identificadordoempresa)
#         instance.empresa.status = empresa_data.get('status', instance.empresa.status)
#         instance.empresa.tipoempresa_id = empresa_data.get('tipoempresa', instance.empresa.tipoempresa_id)
#         instance.empresa.comprimento = empresa_data.get('comprimento', instance.empresa.comprimento)
#         instance.empresa.largura = empresa_data.get('largura', instance.empresa.largura)
#         instance.empresa.imagem = empresa_data.get('imagem', instance.empresa.imagem)
#         instance.empresa.valor = empresa_data.get('valor', instance.empresa.valor)
#         instance.empresa.descricaoempresa = empresa_data.get('descricaoempresa', instance.empresa.descricaoempresa)

#         instance.empresa.save()

#         instance.latitude = validated_data.get('latitude', instance.latitude)
#         instance.longitude = validated_data.get('longitude', instance.longitude)

#         instance.save()

#         return instance

class DetalhesSerializer(serializers.ModelSerializer):
    descricao = DescricaoSerializer()
    lote = LoteSerializer(read_only=True)

    class Meta:
        model = DetalhesModel
        fields = "__all__"
    
    def create(self, validated_data):
        descricao_data = validated_data.pop('descricao')

        descricao, created = Descricaomodel.objects.get_or_create(**descricao_data)

        detalhe = DetalhesModel.objects.create(descricao=descricao, **validated_data)

        return detalhe




class  LoteSolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoteSolicitacaoModel
        fields = "__all__"


class FinalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finalidademodel
        fields = "__all__"


class LoteAtribuicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoteAtribuicaoModel
        fields = "__all__"




class HistoricoLoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoLoteModel
        fields = "__all__"






class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pagamento_atribuicao
        fields = "__all__"