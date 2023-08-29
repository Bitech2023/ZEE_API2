from .models import *
from rest_framework import serializers



class LocalizacaoLoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocalizacaoLoteModel
        fields = "__all__"

class LoteSerializer(serializers.ModelSerializer):
     localizacao = serializers.SerializerMethodField()
     class Meta:
        model = LoteModel
        fields = "__all__"
     def get_localizacao(self, obj):
        try:
            # print(obj)
            response = LocalizacaoLoteModel.objects.filter(loteID=obj)
            print(response)
            return LocalizacaoLoteSerializer(response, many=True).data
        except KeyError:
            return "An error ocurred"

class  LoteSolicitacaoSerializer(serializers.ModelSerializer):
    localizacao = serializers.SerializerMethodField()
    class Meta:
        model = LoteSolicitacaoModel
        fields = "__all__"

class LoteAtribuicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoteAtribuicaoModel
        fields = "__all__"




class HistoricoLoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoLoteModel
        fields = "__all__"


class DescricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descricaomodel
        fields = "__all__"


class LoteEmpresaSerializer( serializers.ModelSerializer):
    class Meta:
        model = LoteEmpresaModel
        fields = "__all__"