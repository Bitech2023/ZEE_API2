from rest_framework import serializers
from empresas.serializers import EmpresaSerializer
from .models import *
from empresas.serializers import ActividadeSerializer
class UserEmpresaSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer()

    class Meta:
            model = UserEmpresaModel
            fields = '__all__'

    def create(self, validated_data):
        empresa_data = validated_data.pop('empresa')

        if empresa_data:
            empresa, created = EmpresaModel.objects.get_or_create(**empresa_data)
            validated_data['empresa'] = empresa

        # empresa, created = EmpresaModel.objects.get_or_create(**empresa_data)
        user_empresa = UserEmpresaModel.objects.create(**validated_data)

        return user_empresa
    
    
class UserSerializer(serializers.ModelSerializer):
        # empresas = serializers.SerializerMethodField()
        class Meta:
            model = User

            fields = "__all__"
                    

        # def get_empresas(self, obj):  
        #     try:
        #         empresaObject = UserEmpresaModel.objects.filter(user=obj)
        #         if empresaObject:
        #              return UserEmpresaSerializer(empresaObject, many=True).data[0]
        #         else:
        #              return{'message':'empty'}
        #     except Exception as error:
        #         return {'error': str(error)}

