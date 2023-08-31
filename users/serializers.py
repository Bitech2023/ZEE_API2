from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = "__all__"

            # def create(self, validated_data):
            # # Encripta a senha antes de criar o usuário
            #     password = validated_data.pop('password')
            #     user = User(**validated_data)
            #     user.set_password(password)
            #     user.save()
            #     return user
