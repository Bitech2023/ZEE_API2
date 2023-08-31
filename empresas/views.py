from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import  IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status


class EmpresaListView(generics.ListAPIView):
    queryset = EmpresaModel.objects.all()
    serializer_class = EmpresaSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    def get(self, request):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            

            for item in serializer.data:
                if item['logo']:
                    item['logo'] = request.build_absolute_uri(item['logo'])
            

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class EmpresaCreateView(generics.CreateAPIView):
    queryset = EmpresaModel.objects.all()
    serializer_class = EmpresaSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]


    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_201_CREATED)
            
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class EmpresaUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmpresaModel.objects.all()
    serializer_class = EmpresaSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]

    def put(self, request, pk):
        try:
              empresa = EmpresaModel.objects.get(id=pk)
  

        except EmpresaModel.DoesNotExist:
            
            return Response(f"Empresa {empresa} não encontrada.", status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(empresa, request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(f"Informacoes da Empresa  {empresa.nome_da_empresa},"" actualizadas com sucesso!", status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, pk):
        try:
              empresa = EmpresaModel.objects.get(id=pk)
              

        except EmpresaModel.DoesNotExist:
            return Response(f"Empresa {empresa} não encontrado.", status=status.HTTP_404_NOT_FOUND)
        
        empresa.delete()

        return Response(f"Empresa:  {empresa} excluida com sucesso",  status=status.HTTP_204_NO_CONTENT)


class FuncionariosCreateView(generics.ListCreateAPIView):
    queryset = FuncionariosModel.objects.all()
    serializer_class = FuncionariosSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

class FuncionariosListView(generics.ListAPIView):
    queryset = FuncionariosModel.objects.all()
    serializer_class = FuncionariosSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]


class NotificacaoGeralCreateView(generics.CreateAPIView):
    queryset = NotificacaoGeralModel.objects.all()
    serializer_class = NotificacaoGeralSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
                 
                # if not request.user.is_staff:
                #     return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)
                
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()                
                return Response({serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response(" message: Erro ao criar a notificacao!", status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class NotificacaoEmpresaCreateView(generics.CreateAPIView):
    queryset = NotificacaoEmpresaModel.objects.all()
    serializer_class = NotificacaoEmpresaSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            if request.user.is_staff:
                return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)
            
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response("message:Erro ao criar a notificacao!", status=status.HTTP_400_BAD_REQUEST) 
            
        except Exception as e:
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)




