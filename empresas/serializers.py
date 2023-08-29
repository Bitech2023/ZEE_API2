from rest_framework import serializers
from .models import *

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaModel
        fields = "__all__"


class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuncionariosModel
        fields = "__all__"


class NotificacaoGeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificacaoGeralModel
        fields = "__all__"

class NotificacaoEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificacaoEmpresaModel
        fields = "__all__"
