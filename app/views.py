from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

class index(APIView):
     def get(self, request):
          try:
            #   Depois (recomendado a partir do DRF 3.2):
             return Response({'message': 'OK.'}, status=status.HTTP_200_OK)
          except:
             return Response({'error': 'Ocorreu algum erro.'}, status=status.HTTP_400_BAD_REQUEST)


class Localizacao(generics.ListCreateAPIView):
     
     queryset = Localizacao.objects.all()
     serializer_class = LocalizacaoSerializer
    

class ImpostoListCreateView(generics.ListCreateAPIView):
   permission_classes = [IsAdminUser]
   authentication_classes = [JWTAuthentication]
   queryset = Impostos.objects.all()
   serializer_class = ImpostosSerializer


class ImpostoEmpresaView(generics.ListCreateAPIView):
   queryset = ImpostoEmpresa.objects.all()
   serializer_class = ImpostoEmpresaSerializer


class SolicitacaoListCreateView(generics.ListCreateAPIView):
   queryset = Solicitacao.objects.all()
   serializer_class = SolicitacaoSerializer


class notificacaogerarLisCreate(generics.ListAPIView):
   queryset = NotificacaoGeral.objects.all()
   serializer_class = NotificacaoGeralSerializer


class NotificacaoEmpresaGeralViewCreate(generics.CreateAPIView):
   queryset = NotificacaoEmpresaSerializer
   serializer_class = NotificacaoEmpresaSerializer


class HistoricoloteListView(generics.ListAPIView):
   queryset  = HistoricoLote.objects.all()
   serializer_class = HistoricoLoteSerializer

class PerfilListView(generics.ListAPIView):
   permission_classes = [IsAuthenticated]
   authentication_classes = [JWTAuthentication]
   queryset = Perfil.objects.all()
   serializer_class = PerfilSerializer