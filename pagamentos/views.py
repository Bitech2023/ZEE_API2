from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import  IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status

class PagamentoListView(generics.ListAPIView):
    queryset = pagamento_atribuicao.objects.all()
    serializer_class = PagamentoSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            
            return Response({"Bem vindo!": serializer.data})
        except:
            return Response("Erro ao processar o servico", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class PagamentoCreateView(generics.CreateAPIView):
    queryset = pagamento_atribuicao.objects.all()
    serializer_class = PagamentoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Pagamento feito com sucesso"},status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        



           

