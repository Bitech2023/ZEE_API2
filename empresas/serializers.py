from rest_framework import serializers
from .models import *
from rest_framework.response import Response
from users.models import UserEmpresaModel


class DocumentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentosModel
        fields = "__all__"  


class DocumentoEmpresaSerializer(serializers.ModelSerializer):
    # empresa = EmpresaSerializer()
    # documentos = DocumentosSerializer()
    class Meta:
        model = DocumentosEmpresaModel
        fields = "__all__"



class ActividadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SectorEmpresaModel
        fields = "__all__"
            

class EmpresaSerializer(serializers.ModelSerializer):
    # actividade2 = serializers.SerializerMethodField()
    class Meta:
        model = EmpresaModel
        fields = "__all__"
    # def get_actividade2(self, obj):
    #     try:
    #         actividadeobj = SectorEmpresaModel.objects.filter(actividade=obj)
    #         print(actividadeobj)
    #         return ActividadeSerializer(actividadeobj,many=True).data
    #     except Exception as e:
    #         print(e)  

class NotificacaoGeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificacaoGeralModel
        fields = "__all__"
class FuncionariosSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(read_only=True)
    class Meta:
 
        model = FuncionariosModel
        fields = "__all__"

class NotificacaoEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificacaoEmpresaModel
        fields = "__all__"

