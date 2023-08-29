from rest_framework import serializers
from .models import EmpresaModel, FuncionariosModel

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaModel
        fields = "__all__"


class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuncionariosModel
        fields = "__all__"
