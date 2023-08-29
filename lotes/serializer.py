from .models import *
from rest_framework import serializers

class LoteSerializer(serializers.ModelSerializer):

     class Meta:
        model = LoteModel
        fields = "__all__"


class  LoteSolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoteSolicitacaoModel
        fields = "__all__"


class LoteAtribuicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoteAtribuicaoModel
        fields = "__all__"


class LocalizacaoLoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalizacaoLoteModel
        fields = "__all__"


class HistoricoLoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoLoteModel
        fields = "__all__"


class DescricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descricaomodel
        fields = "__all__"