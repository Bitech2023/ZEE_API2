from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import  IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response


class UserListView(generics.ListAPIView):
   permission_classes = [IsAdminUser]
   authentication_classes = [JWTAuthentication]
   queryset = User.objects.all()
   serializer_class = UserSerializer

   def get(self, request ):
       try:
         
          if not request.user.is_staff:
                return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)
                           
          queryset = self.get_queryset()
         
          serializer = self.serializer_class(queryset,many=True)
          print(serializer.data)
         
          return Response({"Bem vindo:" :  serializer.data})
       
       except:
          return Response("Erro!")
       
class UserCreateView(generics.ListCreateAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAdminUser]
   authentication_classes = [JWTAuthentication]   
   

   def post(self, request):
        try:
            if not request.user.is_staff:
                return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)
                      
            serializer = self.serializer_class(data=request.data)
                
            if serializer.is_valid():
                   serializer.save() 
                   return Response({"Usuario criado com sucesso! "",":serializer.data })
 
        except:
            return Response({"Erro no servidor ao criar novo  usuario!"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)