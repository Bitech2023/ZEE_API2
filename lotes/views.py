import requests
from users.models import User
from utils.emailTitle import SOLICITACAO_LOTE
from .serializer import *
from .models import *
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import  IsAdminUser,IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
import random
from math import floor
from config.settings import MAPBOX_API_KEY
from config.settings import EMAIL_HOST_USER
from utils.senders import send_email
class Index(APIView):

     def get(self, request):
            try:
                return Response( "message: Bem vindo", status=status.HTTP_200_OK)
            
            except:
                    return Response("message:error: pagina nao encontrada", status=status.HTTP_404_NOT_FOUND)
    

class PagamentoListCreateView(generics.CreateAPIView):
    queryset = pagamento_atribuicao.objects.all()
    serializer_class = PagamentoSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAdminUser]

    def get(self, request):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)

            return Response( serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PagamentoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = pagamento_atribuicao.objects.all()
    serializer_class = LoteSerializer
    #permission_classes = [IsAdminUser]
    #  authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, pk):
        try:
            pagamento = self.queryset.get(id=pk)

            serializer = self.serializer_class(pagamento)

            return Response(serializer.data, status=status.HTTP_200_OK)
   
        except pagamento_atribuicao.DoesNotExist:
            return Response({"message": "pagamento não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def put(self, request, pk ):
         
         try:
          pagamento = pagamento_atribuicao.objects.get(id=pk)  
         except pagamento_atribuicao.DoesNotExist:
            
            return Response("pagamento  não encontrado.", status=status.HTTP_404_NOT_FOUND)

         serializer = self.serializer_class(pagamento, data=request.data)
         if serializer.is_valid():
              serializer.save()
              return Response("Informacoes do pagamento  actualizadas com sucesso!", status=status.HTTP_200_OK)
         else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
    def delete(self, request, pk):
         if not request.user.is_staff:
            return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)
            
         try:
          pagamento = pagamento_atribuicao.objects.get(id=pk)  

         except pagamento_atribuicao.DoesNotExist:
            return Response("pagamento  não encontrado.", status=status.HTTP_404_NOT_FOUND)
    
         pagamento.delete()

         return Response("pagamento excluido com sucesso",  status=status.HTTP_204_NO_CONTENT)
            

class LoteListCreateView(generics.ListCreateAPIView):
    queryset = LoteModel.objects.all()
    serializer_class = LoteSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    def get(self, request):
        try:
            page_num = int(request.GET.get("page", 1))
            limit_num = int(request.GET.get("limit", 100))
            start_num = (page_num - 1) * limit_num
            end_num = limit_num * page_num
            serializer = self.serializer_class(self.queryset[start_num:end_num] , many=True)
            for item in serializer.data:
                if item['imagem']:
                    item['imagem'] = request.build_absolute_uri(item['imagem'])
            
            return Response( serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def generate_random_identifier(self):
        number =random.randint( 100000,600000)
        codigo = (f'LO{number}')
        return codigo

    def post(self, request):
        try:
            # Se o campo codigoLote estiver vazio, gere um valor aleatório
            if 'codigoLote' not in request.data or not request.data['codigoLote']:
                # if request.data['codigoLote'] != 'codigoLote':
                    request.data['codigoLote'] = self.generate_random_identifier()

            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
     
class LoteRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoteModel.objects.all()
    serializer_class = LoteSerializer
    #permission_classes = [IsAdminUser]
    #  authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, pk):
        try:

            lote = LoteModel.objects.filter(id=pk)
            
            serializer = self.serializer_class(lote, many=True)

            for item in serializer.data:
                if item['imagem']:
                    item['imagem'] = request.build_absolute_uri(item['imagem'])
            
            return Response(serializer.data, status=status.HTTP_200_OK)
   
        except LoteModel.DoesNotExist:
            return Response({"message": "Lote não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def put(self, request, pk ):
         
         try:
          lote = LoteModel.objects.get(id=pk)  
          loteid = lote.codigoLote

         except LoteModel.DoesNotExist:
            
            return Response(f"Lote com número {loteid} não encontrado.", status=status.HTTP_404_NOT_FOUND)

         serializer = self.serializer_class(lote, data=request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(f"Informacoes do lote n {loteid} actualizadas com sucesso!", status=status.HTTP_200_OK)
         else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
    def delete(self, request, pk):
         if not request.user.is_staff:
            return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)
            
         try:
          lote = LoteModel.objects.get(id=pk)  
          loteid  = lote.codigoLote
         except LoteModel.DoesNotExist:
            return Response(f"Lote com o número {loteid} não encontrado.", status=status.HTTP_404_NOT_FOUND)
    
         lote.delete()

         return Response(f"lote n {loteid} excluido com sucesso",  status=status.HTTP_204_NO_CONTENT)
        

class TipoLoteCreateListView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = TipoLoteModel.objects.all()
    serializer_class = TipoSerializer

    def get(self, request):
        try:
            tipo = TipoLoteModel.objects.get_queryset()
            serializer = self.serializer_class(tipo, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except TipoLoteModel.DoesNotExist:
            return Response("Nao encontrado", status=status.HTTP_404_NOT_FOUND)  
              
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        try:
            if not request.user.is_staff:
               return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)
            
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            print
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TipoUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = TipoLoteModel.objects.all()
    serializer_class = TipoSerializer

    def retrieve(self, request, *args,pk, **kwargs):
        try:
            tipo = TipoLoteModel.objects.filter(id=pk)

            serializer = self.serializer_class(tipo, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except LoteModel.DoesNotExist:
            return Response({"message": "Lote não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def put(self, request, pk ):
         
         try:
          tipo = TipoLoteModel.objects.get(id=pk)  

         except TipoLoteModel.DoesNotExist:
            
            return Response("Não encontrado.", status=status.HTTP_404_NOT_FOUND)

         serializer = self.serializer_class(tipo, data=request.data)
         if serializer.is_valid():
              serializer.save()
              return Response("Informacoes actualizadas com sucesso!", status=status.HTTP_200_OK)
         
         else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
    def delete(self, request, pk):
        try:
            tipo = TipoLoteModel.objects.get(id=pk)
        
        except TipoLoteModel.DoesNotExist:
            return Response("Nao Encontrado", status=status.HTTP_404_NOT_FOUND)
        
        tipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DescricaoCreateListView(generics.ListCreateAPIView):
   # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = LoteDescricaoModel.objects.all()
    serializer_class = DescricaoSerializer

    def get(self,request, pk):
        try:
                instancia = LoteDescricaoModel.objects.filter(id=pk)
                serializer = self.serializer_class(instancia, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"message1": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class descricaoUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = LoteDescricaoModel.objects.all()
    serializer_class = DescricaoSerializer

    def retrieve(self, request, *args, pk):
        try:
            destalhe = self.queryset.get(id=pk)
            serializer = self.serializer_class(destalhe)

            return Response(serializer.data, status=status.HTTP_200_OK)
   
        except LoteDescricaoModel.DoesNotExist:
            return Response({"message": "Descricao não encontrada."}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request, pk ):
         
         try:
          descricao = LoteDescricaoModel.objects.get(id=pk)  

         except LoteDescricaoModel.DoesNotExist:
            
            return Response({"message": "Descricao não encontrada."}, status=status.HTTP_404_NOT_FOUND)

         serializer = self.serializer_class(descricao, data=request.data)
         if serializer.is_valid():
              serializer.save()
              return Response("Informacoes actualizadas com sucesso!", status=status.HTTP_200_OK)
         
         else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
         
    def delete(self, request, pk):
        try:
            descricao = LoteDescricaoModel.objects.get(id=pk)
        
        except LoteDescricaoModel.DoesNotExist:
            return Response({"message": "Descricao não encontrada."}, status=status.HTTP_404_NOT_FOUND)
        
        descricao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DetalhesCreateListView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = LoteDetalheModel.objects.all()
    serializer_class = LoteDetalheSerializer

    def get(self, request):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return Response( serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"message1": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DetalhesRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = LoteDetalheModel.objects.all()
    serializer_class = LoteDetalheSerializer

    def retrieve(self, request, *args, pk, **kwargs):
        try:
 
            detalhes = self.queryset.filter(loteid=pk)

            serializer = self.serializer_class(detalhes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except LoteDetalheModel.DoesNotExist:
            return Response({"message": "Lote não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

 
class DetalhesUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = LoteDetalheModel.objects.all()
    serializer_class = LoteDetalheSerializer


    def retrieve(self, request, *args, pk, **kwargs):
        try:
 
            detalhes = self.queryset.get(id=pk)

            serializer = self.serializer_class(detalhes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except LoteDetalheModel.DoesNotExist:
            return Response({"message": "Lote não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def put(self, request, pk ):
         
         try:
          descricao = LoteDetalheModel.objects.get(id=pk)  

         except LoteDetalheModel.DoesNotExist:
            
            return Response("Não encontrado.", status=status.HTTP_404_NOT_FOUND)

         serializer = self.serializer_class(descricao, data=request.data)
         if serializer.is_valid():
              serializer.save()
              return Response("Informacoes actualizadas com sucesso!", status=status.HTTP_200_OK)
         
         else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
         
    def delete(self, request, pk):
        try:
            descricao = LoteDetalheModel.objects.get(id=pk)
        
        except LoteDetalheModel.DoesNotExist:
            return Response("Nao Encontrado", status=status.HTTP_404_NOT_FOUND)
        
        descricao.delete()
        return Response("Sucesso!", status=status.HTTP_204_NO_CONTENT)


class LocalizacaoLoteView(generics.ListCreateAPIView):
    queryset = LocalizacaoLoteModel.objects.all()
    serializer_class = LocalizacaoLoteSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    def get(self, request ):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 1000))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num

      
        serializer = self.serializer_class(self.queryset[start_num:end_num] , many=True)

        for item in serializer.data:
            if  item['lote']['imagem']:    
                    item['lote']['imagem'] = request.build_absolute_uri(item['lote']['imagem'] )

        return Response({
            "points": serializer.data
        })
    
    def post(self, request, *args, **kwargs):
        try:
            if not request.user.is_staff:
                return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)
            
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                        serializer.save()
                        return Response({"Lote Criado com sucesso"},status=status.HTTP_202_ACCEPTED)
            else:
                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    
        except Exception as e:
                        return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

     
class LocalizacaoRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    queryset = LocalizacaoLoteModel.objects.all()
    serializer_class = LocalizacaoLoteSerializer

    def retrieve(self, request, *args,pk, **kwargs):
        try:
  
            localizacoes = LocalizacaoLoteModel.objects.filter(lote=pk)
            serializer = self.serializer_class(localizacoes, many=True)

            for item in serializer.data:
                if item['lote']['imagem']:
                    item['lote']['imagem'] = request.build_absolute_uri(item['lote']['imagem'])

            return Response(serializer.data, status=status.HTTP_200_OK)

        except LocalizacaoLoteModel.DoesNotExist:
            return Response({"message": "Localizacao não encontrada."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LocalizacaoLoteUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    queryset = LocalizacaoLoteModel.objects.all()
    serializer_class = LocalizacaoLoteSerializer

    def retrieve(self, request, *args,pk, **kwargs):
        try:
  
            localizacoes = LocalizacaoLoteModel.objects.filter(id=pk)
            serializer = self.serializer_class(localizacoes, many=True)


            for item in serializer.data:
                if item['lote']['imagem']:
                    item['lote']['imagem'] = request.build_absolute_uri(item['lote']['imagem'])

            return Response(serializer.data, status=status.HTTP_200_OK)

        except LocalizacaoLoteModel.DoesNotExist:
            return Response({"message": "Localizacao não encontrada."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            localizacao = LocalizacaoLoteModel.objects.get(id=pk)
  

        except LocalizacaoLoteModel.DoesNotExist:
                return Response("Localizacao nao encontrada", status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(localizacao, data=request.data)
        if serializer.is_valid():
           
            serializer.save()
            # print(serializer.data)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, pk):
        try:
            localizacao = LocalizacaoLoteModel.objects.get(id=pk)
        
        except LocalizacaoLoteModel.DoesNotExist:
                return Response("Localizacao nao encontrada", status=status.HTTP_404_NOT_FOUND)
        
        localizacao.delete()
        return Response("Eliminado Com Sucesso", status=status.HTTP_204_NO_CONTENT)


class GeoLocalizacaoLoteView(generics.ListCreateAPIView):
    queryset = GeoLocalizacaoModel.objects.all()
    serializer_class = GeoLocalizacaoSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    
    def get(self, request ):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 1000))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num

      
        serializer = self.serializer_class(self.queryset[start_num:end_num] , many=True)
 

        # for item in serializer.data:
        #     if  item['lote']['imagem']:    
        #             item['lote']['imagem'] = request.build_absolute_uri(item['lote']['imagem'] )

        return Response({
            "points": serializer.data
        })
    
    def post(self, request, *args, **kwargs):
        try:
            if not request.user.is_staff:
                return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)
            
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                        serializer.save()
                        return Response({"Lote Criado com sucesso"},status=status.HTTP_202_ACCEPTED)
            else:
                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    
        except Exception as e:
                        return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GeoLocalizacaoRetrieveView(generics.RetrieveAPIView):
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    queryset = GeoLocalizacaoModel.objects.all()
    serializer_class = GeoLocalizacaoSerializer

    def retrieve(self, request, *args,pk, **kwargs):
        try:
  
            localizacoes = GeoLocalizacaoModel.objects.filter(lote=pk)
            serializer = self.serializer_class(localizacoes, many=True)

            # for item in serializer.data:
            #     if item['lote']['imagem']:
            #         item['lote']['imagem'] = request.build_absolute_uri(item['lote']['imagem'])

            # print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except GeoLocalizacaoModel.DoesNotExist:
            return Response({"message": "Localizacao não encontrada."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GeoLocalizacaoLoteUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    queryset = GeoLocalizacaoModel.objects.all()
    serializer_class = GeoLocalizacaoSerializer

    def retrieve(self, request, *args,pk, **kwargs):
        try:
  
            localizacoes = GeoLocalizacaoModel.objects.filter(id=pk)
            serializer = self.serializer_class(localizacoes, many=True)


            # for item in serializer.data:
            #     if item['lote']['imagem']:
            #         item['lote']['imagem'] = request.build_absolute_uri(item['lote']['imagem'])

            return Response(serializer.data, status=status.HTTP_200_OK)

        except GeoLocalizacaoModel.DoesNotExist:
            return Response({"message": "Localizacao não encontrada."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            localizacao = GeoLocalizacaoModel.objects.get(id=pk)
  

        except GeoLocalizacaoModel.DoesNotExist:
                return Response("Localizacao nao encontrada", status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(localizacao, data=request.data)
        if serializer.is_valid():
           
            serializer.save()
            # print(serializer.data)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, pk):
        try:
            localizacao = GeoLocalizacaoModel.objects.get(id=pk)
        
        except GeoLocalizacaoModel.DoesNotExist:
                return Response("Localizacao nao encontrada", status=status.HTTP_404_NOT_FOUND)
        
        localizacao.delete()
        return Response("Eliminado Com Sucesso", status=status.HTTP_204_NO_CONTENT)


class LoteSolicitacaoListCreateVier(generics.GenericAPIView):
    queryset = LoteSolicitacaoModel.objects.all()
    serializer_class = LoteSolicitacaoSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
  
        try:
            page_num = int(request.GET.get("page", 1))
            limit_num = int(request.GET.get("limit", 100))
            start_num = (page_num - 1) * limit_num
            end_num = limit_num * page_num

      
            serializer = self.serializer_class(self.queryset[start_num:end_num] , many=True)
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

        except Exception as e:
            return Response({"message": "Erro ao recuperar os dados.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        try:

            data=request.data
            loteId = request.data["loteId"]
            finalidades = request.data["finalidades"]
            loteData = LoteModel.objects.filter(id=loteId).get()
            tempo = request.data['tempo']
            valorLote = loteData.valor
            precoLote = valorLote * tempo
            # Salvar a solicitacao
            SolicitacaoInstance = LoteSolicitacaoModel()
            SolicitacaoInstance.userId = request.user
            SolicitacaoInstance.loteId = loteData
            SolicitacaoInstance.valor = precoLote
            SolicitacaoInstance.tempo = tempo
            
            SolicitacaoInstance.save() 
            
            # Salvar as finalidades
            finalidade_descriptions = []
            
            
            for finalidade in finalidades:
                tipoData = TipoLoteModel.objects.get(id=finalidade["tipoId"])
                finalidadeInstace = FinalidadeSolicitacaoModel()
                finalidadeInstace.tipoId = tipoData
                finalidadeInstace.solicitacao = SolicitacaoInstance
                finalidadeInstace.save()
                finalidade_descriptions.append(finalidadeInstace.tipoId)
            print(finalidade_descriptions)
            #  Enviar Email para o usuario Cadastrado
            
            email_to = request.user.email
            lote_data = {
            "codigoLote":SolicitacaoInstance.loteId.codigoLote,
            "preco": precoLote,
            "duracao":tempo,
            "descricao":SolicitacaoInstance.loteId.descricaolote,
            "imagem":SolicitacaoInstance.loteId.imagem,
            "email":email_to,
            "finalidade":finalidade_descriptions
            # "finalidade":finalidadeInstace
            }
                
            try:
                send_email(to=email_to,
                        subject=SOLICITACAO_LOTE,
                        template_name="index.html",
                        context=lote_data)
                   
                return Response({f"message": "Solicitação feita com sucesso", "Data":data, "OBS Foi lhe enviado um Email para" :request.user.email },status=status.HTTP_201_CREATED)
            except Exception as e:
                    print(e)
                    return Response({"message": f"Error sending email: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  
                          
        except Exception as e:
            print(e)
            # Trate exceções de maneira adequada e forneça uma mensagem de erro
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class LoteSolicitacaoRetrieView(generics.RetrieveAPIView):
    queryset = LoteSolicitacaoModel.objects.all()
    serializer_class = LoteSolicitacaoSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args):
        try:
            
            lote = LoteSolicitacaoModel.objects.filter(userId=request.user.id) 
            serializer = self.serializer_class(lote, many=True)

            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
        except LoteSolicitacaoModel.DoesNotExist:
            return Response("message" "Solicitacao não encontrada.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class LoteSolicitacaoRetrievDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoteSolicitacaoModel.objects.all()
    serializer_class = LoteSolicitacaoSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, pk):
        try:
            lote = LoteSolicitacaoModel.objects.filter(id=pk) 
            serializer = self.serializer_class(lote, many=True)

            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
        except LoteSolicitacaoModel.DoesNotExist:
            return Response("message" "Solicitacao não encontrada.", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


    def put(self, request, pk, *args):
        try:
               solicitacao = LoteSolicitacaoModel.objects.get(id=pk)

        except LoteSolicitacaoModel.DoesNotExist:
                return Response("A solicitacao nao existe", status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(solicitacao ,data=request.data)

        if serializer.is_valid():
                serializer.save()
                return Response("informacoes da solicitacao actualizadas com sucesso!", status=status.HTTP_202_ACCEPTED)
        else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, reuqest, pk):
        try:
            solicitacao = LoteSolicitacaoModel.objects.get(id=pk)

        except LoteSolicitacaoModel.DoesNotExist:
            return Response({"Nao existe nenhuma solicitacao" }, status=status.HTTP_404_NOT_FOUND)


        solicitacao.delete()

        return Response("Solicitacao eliminda com exito  eliminda com sucesso!")    

class FinalidadeSolicitacaoListCrateView(generics.ListCreateAPIView):
    queryset = FinalidadeSolicitacaoModel.objects.all()
    serializer_class = FinalidadeSolitacaoSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]


    def get(self, request, *args, **kwargs):
        try:
            page_num = int(request.GET.get("page", 1))
            limit_num = int(request.GET.get("limit", 100))
            start_num = (page_num - 1) * limit_num
            end_num = limit_num * page_num
            queryset = self.get_queryset()       
            serializer = self.serializer_class(queryset[start_num:end_num], many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except FinalidadeSolicitacaoModel.DoesNotExist:
            return Response("Nao existem finalidades", status=status.HTTP_401_UNAUTHORIZED)

            
    def post(self, request, *args, **kwargs):
        try:

            serializer = self.serializer_class(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FinalidadeSolicitacaoRetrieveView(generics.RetrieveAPIView):
    queryset = FinalidadeSolicitacaoModel.objects.all()
    serializer_class = FinalidadeSolitacaoSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]

    def retrieve(self, request, pk):
        try:
            

            finalidade = self.queryset.filter(solicitacao=pk)
            serializer = self.serializer_class(finalidade, many=True)
            # print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except FinalidadeSolicitacaoModel.DoesNotExist:

            return Response(f"Nao existe nehuma finalidade ", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
             print(e)
        
             return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class FinalidadeSolicitacaoUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FinalidadeSolicitacaoModel.objects.all()
    serializer_class = FinalidadeSolitacaoSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]

    def retrieve(self, request, pk):
        try:

            finalidade = self.queryset.filter(id=pk)
            serializer = self.serializer_class(finalidade, many=True)
            # print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except FinalidadeSolicitacaoModel.DoesNotExist:

            return Response(f"Nao existe", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
             print(e)
        
             return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def put(self, request, pk):
        try:
              finalidade = FinalidadeSolicitacaoModel.objects.get(id=pk)

        except FinalidadeSolicitacaoModel.DoesNotExist:
                return Response("A finalidade do lote com o id  nao existe" , status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(finalidade, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,"Finalidade criada com sucesso!", status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        

    def delete(self, request, pk):
            try:
                finalidade = FinalidadeSolicitacaoModel.objects.get(id=pk)

            except FinalidadeSolicitacaoModel.DoesNotExist:
                return Response("finalidade do lote nao existe no sistema", status=status.HTTP_404_NOT_FOUND)
        
            finalidade.delete()

            return Response("finalidade do lote  eliminda com sucesso!", status=status.HTTP_204_NO_CONTENT)   

 


class LoteAtribicaoListCreateView(generics.ListCreateAPIView):
    queryset = LoteAtribuicaoModel.objects.all()
    serializer_class = LoteAtribuicaoSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    
    def get(self, request):
        try:
            page_num = int(request.GET.get("page", 1))
            limit_num = int(request.GET.get("limit", 100))
            start_num = (page_num - 1) * limit_num
            end_num = limit_num * page_num
            serializer = self.serializer_class(self.queryset[start_num:end_num] , many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except:
            return Response({"Sao necessarias credenciais de usario"}, status=status.HTTP_401_UNAUTHORIZED)
        

    def post(self, request, *args, **kwargs):
        try:

            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                 return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

        
        except Exception as e:
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class LoteAtribuicaoUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoteAtribuicaoModel.objects.all()
    serializer_class = LoteAtribuicaoSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]

    def retrieve(self, request, pk):
        try:
            atribuicao = self.queryset.filter(id=pk)
            
            serializer = self.serializer_class(atribuicao, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except LoteAtribuicaoModel.DoesNotExist:

            return Response("Nao existe atribuicao para este lote", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
             print(e)
        
             return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def put(self, request, pk):
        try:
              atribuicao =LoteAtribuicaoModel.objects.get(id=pk)


        except LoteAtribuicaoModel.DoesNotExist:
                return Response("A atribuicao do lote com o id  nao existe" , status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(atribuicao, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response("Atribuicao do lote com o id  editada com sucesso", status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        

    def delete(self, request, pk):
            try:
                atribuicao = LoteAtribuicaoModel.objects.get(id=pk)

            except LoteAtribuicaoModel.DoesNotExist:
                return Response("Atribuicao do lote nao existe no sistema", status=status.HTTP_404_NOT_FOUND)
        
            atribuicao.delete()

            return Response("Solicitacao do lote com o id  eliminda com sucesso!", status=status.HTTP_204_NO_CONTENT)   


class HistoricoLoteListView(generics.ListAPIView):
    queryset = HistoricoLoteModel.objects.all()
    serializer_class = HistoricoLoteSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    def get(self, request): 
        try:
            page_num = int(request.GET.get("page", 1))
            limit_num = int(request.GET.get("limit", 100))
            start_num = (page_num - 1) * limit_num
            end_num = limit_num * page_num
            serializer = self.serializer_class(self.queryset[start_num:end_num] , many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except :
                return Response("Sao necessarias credenciais de usario!", status=status.HTTP_401_UNAUTHORIZED)


class HistoricoLoteCreateView(generics.ListCreateAPIView):
    queryset = HistoricoLoteModel.objects.all()
    serializer_class = HistoricoLoteSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            else:
                 return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

        
        except Exception as e:
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class HistoricoLoteUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoricoLoteModel.objects.all()
    serializer_class = HistoricoLoteSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]

    def put(self, request, pk):
        try:
            historico = HistoricoLoteModel.objects.get(id=pk)

        except HistoricoLoteModel.DoesNotExist:
            return Response("O Historico do lote solicitado  nao existe" , status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(historico, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    def delete(self, request, pk):
        try:
            serializer = HistoricoLoteModel.objects.get(id=pk)

        except HistoricoLoteModel.DoesNotExist:
            return Response("O Historico do lote solicitado  nao existe" , status=status.HTTP_404_NOT_FOUND)
        
        serializer.delete()
        return Response("Historico do Lote Eliminado com Sucesso", status=status.HTTP_204_NO_CONTENT)
    

class LoteEmpresaListCreate(generics.ListCreateAPIView):
    queryset = LoteEmpresaModel.objects.all()
    serializer_class = LoteEmpresaSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    def get(self, request):
        try:
            page_num = int(request.GET.get("page", 1))
            limit_num = int(request.GET.get("limit", 100))
            start_num = (page_num - 1) * limit_num
            end_num = limit_num * page_num
            serializer = self.serializer_class(self.queryset[start_num:end_num] , many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except LoteEmpresaModel.DoesNotExist:
            print("Lote da Empresa nao encontrado!", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoteEmpresaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoteEmpresaModel.objects.all()
    serializer_class = LoteEmpresaSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]

    def retrieve(self, request, pk):
        try:
            loteEmpresa = self.queryset.filter(lote=pk)
            serializer = self.serializer_class(loteEmpresa, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except LoteAtribuicaoModel.DoesNotExist:

            return Response("Nao existe uma empresa com este lote", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
             print(e)
        
             return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def put(self, request, pk):
        try:
              loteEmpresa = LoteEmpresaModel.objects.get(id=pk)

        except LoteEmpresaModel.DoesNotExist:
                return Response("Lote da Empresa  nao existe" , status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(loteEmpresa, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response("Empresa Lote editada com sucesso", status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        

    def delete(self, request, pk):
            try:
                loteEmpresa = LoteEmpresaModel.objects.get(id=pk)

            except LoteEmpresaModel.DoesNotExist:
                return Response("Atribuicao do lote nao existe no sistema", status=status.HTTP_404_NOT_FOUND)
        
            loteEmpresa.delete()

            return Response("Solicitacao do lote com o id  eliminda com sucesso!", status=status.HTTP_204_NO_CONTENT)   


class LoteImageListCreateView(generics.ListCreateAPIView):
    queryset = Loteimage.objects.all()
    serializer_class = LoteImagerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    def get(self, request):
        try:
            page_num = int(request.GET.get("page", 1))
            limit_num = int(request.GET.get("limit", 100))
            start_num = (page_num - 1) * limit_num
            end_num = limit_num * page_num
            serializer = self.serializer_class(self.queryset[start_num:end_num] , many=True)
            for item in serializer.data:
                if item['imagem']:
                    item['imagem'] = request.build_absolute_uri(item['imagem'])

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Loteimage.DoesNotExist:
            print({"Lote Imagem nao encontrada!"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

     
class LoteImagemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loteimage.objects.all()
    serializer_class = LoteImagerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]

    def retrieve(self, request, pk):
        try:
            titulo = self.queryset.filter(loteId=pk)
            serializer = self.serializer_class(titulo, many=True)
            for item in serializer.data:
                if item['imagem']:
                    item['imagem'] = request.build_absolute_uri(item['imagem'])

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Loteimage.DoesNotExist:

            return Response("Nao existe uma imagem associada a  lote", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
             print(e)
        
             return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def put(self, request, pk):
        try:
              loteEmpresa = Loteimage.objects.filter(id=pk)

        except Loteimage.DoesNotExist:
                return Response("Imagem do lote  nao existe" , status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(loteEmpresa, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response("Imagem do Lote editada com sucesso", status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        

    def delete(self, request, pk):
            try:
                titulo = Loteimage.objects.get(id=pk)

            except Loteimage.DoesNotExist:
                return Response("Imagem do lote nao existe no banco de dados", status=status.HTTP_404_NOT_FOUND)
        
            titulo.delete()

            return Response("imagem deletada com sucesso!", status=status.HTTP_204_NO_CONTENT)   


# Crud Completo do Titluo dos documentos do  lote
class DocumentoTituloListcreateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = DocumentoTituloModel.objects.all()
    serializer_class = DocumentoTituloSerializer

    def get(self, request):
        try:
            page_num = int(request.GET.get("page", 1))
            limit_num = int(request.GET.get("limit", 100))
            start_num = (page_num - 1) * limit_num
            end_num = limit_num * page_num
            serializer = self.serializer_class(self.queryset[start_num:end_num] , many=True)
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao Listar titulos de Documentos.", "error": str(e)},
                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():

                serializer.save()
                return Response({"data" : [ serializer.data ] }, status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
        except Exception as e:
            print(e)
            # Trate exceções de maneira adequada e forneça uma mensagem de erro
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DocumentoTitluoRetrieveDeleteUpdateView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = DocumentoTituloModel.objects.all()
    serializer_class = DocumentoTituloSerializer

    def get(self, request,pk):
        try:
            page_num = int(request.GET.get("page", 1))
            limit_num = int(request.GET.get("limit", 100))
            start_num = (page_num - 1) * limit_num
            end_num = limit_num * page_num
            serializer = self.serializer_class(self.queryset[start_num:end_num] , many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({f"Erro ao Porocessar:",str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except DocumentoTituloModel.DoesNotExist:
            return Response({"message": "Nome não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk ):
         
        try:
            documento = DocumentoTituloModel.objects.get(id=pk) 

            serializer = self.serializer_class(documento, data=request.data)
        
            if serializer.is_valid():
              serializer.save()
              return Response({f"Informacoes do Documento  actualizadas com sucesso!":serializer.data}, status=status.HTTP_200_OK)
            else:
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DocumentoTituloModel.DoesNotExist:
            
            return Response("Documento  não encontrado.", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
         
         if not request.user.is_staff:
            return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)
            
         try:
          documento = DocumentoTituloModel.objects.get(id=pk)  

         except DocumentoTituloModel.DoesNotExist:
            return Response("documento  não encontrado.", status=status.HTTP_404_NOT_FOUND)
    
         documento.delete()

         return Response("documento excluido com sucesso",  status=status.HTTP_204_NO_CONTENT)
            
        # Crud Completo dos Documentos do lote

class DocumentoLoteListcreateView(generics.GenericAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = DocumentoLoteModel.objects.all()
    serializer_class = DocumentoLoteSerializer

    def get(self, request):
        try:
            page_num = int(request.GET.get("page", 1))
            limit_num = int(request.GET.get("limit", 100))
            start_num = (page_num - 1) * limit_num
            end_num = limit_num * page_num
            serializer = self.serializer_class(self.queryset[start_num:end_num] , many=True)
            for item in serializer.data:
                    if item["documento"] :
                        item["documento"] = request.build_absolute_uri(item["documento"])    

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self,request, *args):
        try:
                serializer = self.serializer_class(data=request.data)
                
                if serializer.is_valid():
                    serializer.save()
                    print(serializer.data)
                    return Response({"data" : [ serializer.data ] }, status=status.HTTP_201_CREATED)

                else:
                    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DocumentoLoteRetrieveDeleteUpdateView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = DocumentoLoteModel.objects.all()
    serializer_class = DocumentoLoteSerializer

    def get(self, request,pk):
        try:
            documneto = DocumentoLoteModel.objects.filter(loteId=pk)
            serializer = self.serializer_class(documneto,many=True)

            for item in serializer.data:
                if item["documento"]:
                    item["documento"] = request.build_absolute_uri(item["documento"])
                
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({f"Erro ao Porocessar:",str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except DocumentoLoteModel.DoesNotExist:
            return Response({"message": "Documento Nao encontrado."}, status=status.HTTP_404_NOT_FOUND)
    

    def put(self, request, pk ):
         
        try:
            documento = DocumentoLoteModel.objects.get(id=pk) 

            serializer = self.serializer_class(documento, data=request.data)
        
            if serializer.is_valid():
              serializer.save()
              return Response({f"Informacoes do Documento  actualizadas com sucesso!":serializer.data}, status=status.HTTP_200_OK)
            else:
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DocumentoLoteModel.DoesNotExist:
            
            return Response("Documento  não encontrado.", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
         
         if not request.user.is_staff:
            return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)
            
         try:
          documento = DocumentoLoteModel.objects.get(id=pk)  

         except DocumentoLoteModel.DoesNotExist:
            return Response("documento  não encontrado.", status=status.HTTP_404_NOT_FOUND)
    
         documento.delete()

         return Response("documento excluido com sucesso",  status=status.HTTP_204_NO_CONTENT)
            
        
       
# Integracao com api do mapbox para obter a distancia do usuario

class GeoCodeView(APIView):
    serializer_class = LocalizacaoLoteSerializer

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 100))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num

        latitude = request.query_params.get('lat')
        longitude = request.query_params.get('lon')
        modo = request.query_params.get('modo')
       
        if not (latitude and longitude):
            return Response({'error': 'Query parameters "lat" and "lon" are required'}, status=status.HTTP_400_BAD_REQUEST)

        
        instancia = LocalizacaoLoteModel.objects.all()
        serializer = self.serializer_class(instancia[start_num:end_num],many=True)
        localizacoes = serializer.data
        access_token = MAPBOX_API_KEY
        origem = f"{longitude},{latitude}"

        result = []

        for localizacao in localizacoes:
            destinolongitude = localizacao['longitude']
            destinolatitude = localizacao['latitude']
            destino = f"{destinolongitude},{destinolatitude}"
            
            id = localizacao['id']
            # lote = localizacao['lote']
            codigoLote = localizacao['lote']['codigoLote']
            loteId = localizacao['lote']['id']
            imagem = localizacao['lote']['imagem']
            Status = localizacao['lote']['status']
            preco = localizacao['lote']['valor']
            itens = serializer.data
            
            for item in itens:
                if item['lote']['imagem']:
                    imagem =item['lote']['imagem']
            imagem = request.build_absolute_uri(imagem)

            try:
                base_url = f"https://api.mapbox.com/directions/v5/mapbox/{modo}/{origem};{destino}"
                params = {'access_token': access_token}
                response = requests.get(base_url, params=params)
                response.raise_for_status()  # Lidar com erros de solicitação

                data = response.json()
                duracao = data['routes'][0]['duration']
                distancia = data['routes'][0]['distance']
                sumario = data['routes'][0]['legs'][0]['summary']
                
                localizacao_data = {
                    "id":id,
                    "latitude": destinolatitude,
                    "longitude": destinolongitude,
                    # 'lote':lote,
                     "codigoLote ":  codigoLote,
                     'loteId':loteId,
                     "Status":Status,
                     "imagem" : imagem,
                     'preco':preco
                    
                }

                if distancia > 0 and duracao > 0:
                    # Cálculos de duração, distância e velocidade

                    dia = floor(duracao / 86400)
                    hora = floor((duracao % 86400) / 3600)
                    minutos = round((duracao % 3600) / 60)
                    formatarDuracao = ''
                    if dia > 0: formatarDuracao += f"{dia}d "
                    if hora > 0: formatarDuracao += f"{hora}h e "
                    formatarDuracao += f"{minutos}min"

                    distanciaKm = distancia / 1000
                    velocidadeKm = distanciaKm / (duracao / 3600)
                    velocidadems = (distanciaKm / 1000) / duracao

                    if distancia > 1000:
                        localizacao_data["distancia"] = "{:.{}f}Km".format(distanciaKm, 2)
                        localizacao_data["velocidade"] = "{:.{}f}Km/h".format(velocidadeKm, 2)
                    if distancia < 1000:
                        localizacao_data["distancia"] = "{:.{}f}m".format(distancia, 2)
                        localizacao_data["velocidade"] = "{:.{}f}m/s".format((velocidadems), 5)

                    localizacao_data["duracao"] = formatarDuracao

                    if sumario == '' or sumario == None:
                        localizacao_data['sumario'] = "Nao foi encontrado nenhum ponto de referencia"

                    else:
                        localizacao_data['sumario'] = sumario
                    
                else:
                    localizacao_data["duracao"] = 0
                    localizacao_data["distancia"] = 0
                    localizacao_data["velocidade"] = 0
                    localizacao_data['sumario'] = sumario

                result.append(localizacao_data)

            except Exception as e:
                # Trate exceções de solicitação, por exemplo, log ou retorne erro personalizado
                return Response({'error': f'Erro na solicitação à API do Mapbox: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"Routes": result})
