from empresas.serializers import EmpresaSerializer
from lotes.models import *
from rest_framework import serializers
from rest_framework.response import Response
from users.serializers import UserSerializer


class LoteSerializer(serializers.ModelSerializer):
    documentos = serializers.SerializerMethodField()
 

    class Meta:
        model = LoteModel
        # fields = ['id','codigoLote',"status","data_disponibilidade","comprimento","largura","imagem","valor","descricaolote","documentos"]
        fields = "__all__"

    def get_documentos(self,obj):
        try:
            documentosobj = DocumentoLoteModel.objects.filter(loteId=obj)
            
            return DocumentoLoteSerializer(documentosobj,many=True).data   #DocumentoLoteModel(documentosobj,many=True) 

        except Exception as e:
            print(e)
            return Response("Error: ",str(e))
        

class LoteEmpresaSerializer( serializers.ModelSerializer):
    empresa = EmpresaSerializer(read_only=True)
    lote = LoteSerializer(read_only=True)
    class Meta:
        model = LoteEmpresaModel
        fields = "__all__"        

class LocalizacaoLoteSerializer(serializers.ModelSerializer):
    lote = LoteSerializer()
    
    class Meta:
        model = LocalizacaoLoteModel
        fields = "__all__"

    def create(self, validated_data):
        lote_data = validated_data.pop('lote')

        lote, created = LoteModel.objects.get_or_create(**lote_data)

        lote = LocalizacaoLoteModel.objects.create(lote=lote, **validated_data)

        return lote

    def update(self, instance, validated_data):
        lote_data = validated_data.pop('lote')
        
        instance.lote.identificadordolote = lote_data.get('identificadordolote', instance.lote.identificadordolote)
        instance.lote.status = lote_data.get('status', instance.lote.status)
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
    
class GeoLocalizacaoSerializer(serializers.ModelSerializer):
    # lote = serializers.SerializerMethodField()
    class Meta:
        model = GeoLocalizacaoModel
        fields = '__all__'

        # def get_lote(self, obj):
        #     loteobj = serializers.SerializerMethodField()

        #     return LoteSerializer(loteobj, many=True)

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

class TipoSerializer(serializers.ModelSerializer):
    # finalidade = serializers.SerializerMethodField()
    
    class Meta:
        model = TipoLoteModel
        fields = '__all__'
    # def get_finalidade(self, obj):
    #     try:
    #         tipoobj = FinalidadeSolicitacaoModel.objects.filter(tipoId=obj)
    #         print(tipoobj)
    #         return FinalidadeSolitacaoSerializer(tipoobj,many=True).data
    #     except Exception as e:
    #         print(e)        

class LoteSolicitacaoSerializer(serializers.ModelSerializer):
    # loteId = serializers.SerializerMethodField()
    finalidades = serializers.SerializerMethodField()
    class Meta:
        model = LoteSolicitacaoModel
        fields = '__all__'
    
    def get_finalidades(self, obj):
        try:
            finalidadesobj = FinalidadeSolicitacaoModel.objects.filter(solicitacao=obj)
            
            return FinalidadeSolitacaoSerializer(finalidadesobj,many=True).data
        
        except Exception as e:
            print(e)
            return Response("Error",str(e))
    

class FinalidadeSolitacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FinalidadeSolicitacaoModel
        fields = '__all__'


class LoteAtribuicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoteAtribuicaoModel
        fields = "__all__"


class LoteImagerializer(serializers.ModelSerializer):
    # lote = serializers.SerializerMethodField()
    class Meta:
        model = Loteimage
        fields = '__all__'


    # def get_lote(self, obj):
    #     loteobj = LoteModel.objects.filter(loteimage=obj)
    #     return LoteSerializer(loteobj,many=True)

class HistoricoLoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoLoteModel
        fields = "__all__"

class DescricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoteDescricaoModel
        fields = '__all__'


class LoteDetalheSerializer(serializers.ModelSerializer):
    # descricao = DescricaoSerializer()
    # descricao = serializers.SerializerMethodField()
    class Meta:
        
        model = LoteDetalheModel
        fields = '__all__'

    # def create(self, validated_data):
    #     descricao_data = validated_data.pop('descricao')

    #     descricao, created = LoteDescricaoModel.objects.get_or_create(**descricao_data)

    #     descricao = LoteDetalheModel.objects.create(descricao=descricao, **validated_data)
    #     return descricao

    # def get_descricao(self, obj):
    #    descricaoObj = serializers.SerializerMethodField()
    #    return DescricaoSerializer(descricaoObj, many=True)


class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pagamento_atribuicao
        fields = "__all__"


class DocumentoTituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentoTituloModel
        fields = "__all__"

    
class DocumentoLoteSerializer(serializers.ModelSerializer):
    # loteId = LoteSerializer(read_only=True)
    class Meta:
        model = DocumentoLoteModel
        fields = "__all__"

