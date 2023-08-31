from rest_framework import generics
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password  


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListView(generics.ListAPIView):
#    permission_classes = [IsAdminUser]
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
        

       
class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
   
    def post(self, request):
        try:
            # if not request.user.is_staff:
            #      return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)
                      
            serializer = self.serializer_class(data=request.data)
            
            if serializer.is_valid():
                
                # Encripta a senha antes de salvar
                serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
                serializer.save()
                print(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
        except Exception as error:
            print(error)
            return Response({"Erro no servidor ao criar novo usuário!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


