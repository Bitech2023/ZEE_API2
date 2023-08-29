from rest_framework import serializers
from .models import *

class NotificacaoGeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificacaoGeralModel
        fields = "__all__"

class NotificacaoEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificacaoEmpresaModel
        fields = "__all__"