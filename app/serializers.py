from rest_framework import serializers
from .models import *


class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = "__all__"


class ImpostosSerializer(serializers.ModelSerializer):
    class Meta:
         model = Impostos
         fields ="__all__"


class ImpostoEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpostoEmpresa
        fields = "__all__"


class SolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitacao
        fields = "__all__"


class NotificacaoGeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificacaoGeral
        fields = "__all__"

class NotificacaoEmpresaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = NotificacaoEmpresa
        fields = "__all__"


class HistoricoLoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoLote
        fields = "__all__"


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = "__all__"


