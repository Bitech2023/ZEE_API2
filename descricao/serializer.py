from rest_framework import serializers
from models import Descricaomodel


class DescricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descricaomodel
        fields = "__all__"