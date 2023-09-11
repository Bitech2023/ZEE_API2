from rest_framework import generics
from rest_framework import status
from .models import User,UserEmpresaModel
from .serializers import UserSerializer,UserEmpresaSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password  


class UserListCreateView(generics.ListCreateAPIView):
#    permission_classes = [IsAuthenticated]
#    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            
            for item in serializer.data:
                if item['foto']:
                    item['foto'] = request.build_absolute_uri(item['foto'])
            

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def post(self, request):
        try:
            # if not request.user.is_staff:
            #      return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)
                      
            serializer = self.serializer_class(data=request.data)
            
            if serializer.is_valid():

                serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
                
                serializer.save()

                print(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
        except Exception as error:
            print(error)
            return Response({"Erro no servidor ao criar novo usuário!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   

class UserRetrieveView(generics.RetrieveAPIView):
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer    

    def retrieve(self, request, pk):
        try:
            # Filtrar o usuário pelo ID
            user = self.queryset.get(id=pk)
            
            # Serializar o único objeto de usuário
            serializer = self.serializer_class(user)
            
            if serializer.data['foto']:
                serializer.data['foto'] = request.build_absolute_uri(serializer.data['foto'])
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except User.DoesNotExist:
            return Response({"message": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class UserUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, pk):
        try:
            user = User.objects.get(id=pk)

        except User.DoesNotExist:
            return Response("O user do lote solicitado  nao existe" , status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        serializer = self.serializer_class(user, data=request.data)

        if serializer.is_valid():

            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
        

    def delete(self, request,  pk):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response("Usuario nao encontrado!", status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response("Usuario deletado com sucesso", status=status.HTTP_204_NO_CONTENT)



class USerEmpresaListCreate(generics.ListCreateAPIView):
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    queryset = UserEmpresaModel.objects.all()
    serializer_class = UserEmpresaSerializer

    def get(self, request):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            
            # for item in serializer.data:
            #     if item['foto']:
            #         item['foto'] = request.build_absolute_uri(item['foto'])
            

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def post(self, request):
        try:
            # if not request.user.is_staff:
            #      return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)
                      
            serializer = self.serializer_class(data=request.data)
        
            if serializer.is_valid():

                # serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
                serializer.save()

                print(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
        except Exception as error:
            print(error)
            return Response({"Erro no servidor ao criar novo usuário!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   

class UserEmpresaRetrieveView(generics.RetrieveAPIView):
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    queryset = UserEmpresaModel.objects.all()
    serializer_class = UserEmpresaSerializer


    def retrieve(self, request, pk):
        try:
            # Filtrar o usuário pelo ID
            user = self.queryset.get(id=pk)
            
            # Serializar o único objeto de usuário
            serializer = self.serializer_class(user)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except User.DoesNotExist:
            return Response({"message": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class UserEmpresaUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    queryset = UserEmpresaModel.objects.all()
    serializer_class = UserEmpresaSerializer

    def put(self, request, pk):
        try:
            userEmpresa = UserEmpresaModel.objects.get(id=pk)
        
        except UserEmpresaModel.DoesNotExist:
            return Response("Usuario nao encontrado", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
             print(e)
             return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        serializer = self.serializer_class(userEmpresa, data=request.data)
        if serializer.is_valid():
            serializer.save
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            print(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self, reuqest, pk):
        try:
            userEmpresa = UserEmpresaModel.objects.get(id=pk)
        
        except UserEmpresaModel.DoesNotExist:
            return Response("Usuario nao encontrado", status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
             print(e)
             return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        userEmpresa.delete()
        return Response("Usuario Eliminado com Sucesso", status=status.HTTP_204_NO_CONTENT)
   

