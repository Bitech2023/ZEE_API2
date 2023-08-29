from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
class NotificacaoGeralCreateView(generics.CreateAPIView):

    queryset = NotificacaoGeralModel.objects.all()
    serializer_class = NotificacaoGeralSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
                 
                # if not request.user.is_staff:
                #     return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)
                
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()                
                return Response({"Notificacao criada com sucesso: ":serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response(" message: Erro ao criar a notificacao!", status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class NotificacaoEmpresaCreateView(generics.CreateAPIView):
    queryset = NotificacaoEmpresaModel.objects.all()
    serializer_class = NotificacaoEmpresaSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            if request.user.is_staff:
                return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)
            
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Notificacao criada com sucesso: ":serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response("message:Erro ao criar a notificacao!", status=status.HTTP_400_BAD_REQUEST) 
            
        except Exception as e:
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)



