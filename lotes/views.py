from users.models import User
from .serializer import *
from .models import *
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import  IsAdminUser,IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status


def get(self, request):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            
            return Response(serializer.data)
        except:
            return Response("Erro ao processar o servico", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class PagamentoCreateView(generics.CreateAPIView):
    queryset = pagamento_atribuicao.objects.all()
    serializer_class = PagamentoSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAdminUser]

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
class Index(APIView):

     def get(self, request):
            try:
                return Response( "message: Bem vindo", status=status.HTTP_200_OK)
            
            except:
                    return Response("message:error: pagina nao encontrada", status=status.HTTP_404_NOT_FOUND)
    

     
class LoteListView(generics.ListAPIView):
    queryset = LoteModel.objects.all()
    serializer_class = LoteSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    def get(self, request):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)

            for item in serializer.data:
                if item['imagem']:
                    item['imagem'] = request.build_absolute_uri(item['imagem'])
            
            return Response( serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoteRetrieveView(generics.RetrieveAPIView):
    queryset = LoteModel.objects.all()
    serializer_class = LoteSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]


    def retrieve(self, request, *args, pk):
        try:
            lote = self.queryset.get(id=pk)
            serializer = self.serializer_class(lote)

            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
        except LoteModel.DoesNotExist:
            return Response({"message": "Lote não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoteCreateView(generics.ListCreateAPIView):
    queryset = LoteModel.objects.all()
    serializer_class = LoteSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]


    def post(self, request, *args, **kwargs):
        try:
            if not request.user.is_staff:
                return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)

            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():

                serializer.save()
                print(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class LoteUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoteModel.objects.all()
    serializer_class = LoteSerializer
    #permission_classes = [IsAdminUser]
    #  authentication_classes = [JWTAuthentication]

    def put(self, request, pk ):
         
         try:
          lote = LoteModel.objects.get(id=pk)  
          loteid = lote.identificadordolote

         except LoteModel.DoesNotExist:
            
            return Response(f"Lote com número {loteid} não encontrado.", status=status.HTTP_404_NOT_FOUND)

         serializer = self.serializer_class(lote, data=request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(f"Informacoes do lote n {lote.identificadordolote} actualizadas com sucesso!", status=status.HTTP_200_OK)
         else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
    def delete(self, request, pk):
         if not request.user.is_staff:
            return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)
            
         try:
          lote = LoteModel.objects.get(id=pk)  
          loteid  = lote.identificadordolote
         except LoteModel.DoesNotExist:
            return Response(f"Lote com o número {loteid} não encontrado.", status=status.HTTP_404_NOT_FOUND)
    
         lote.delete()

         return Response(f"lote n {lote.identificadordolote} excluido com sucesso",  status=status.HTTP_204_NO_CONTENT)
        

class TipoLoteCreateListView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = TipoLote.objects.all()
    serializer_class = TipoLoteSerializer

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
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TipoLoteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = TipoLote.objects.all()
    serializer_class = TipoLoteSerializer

    def put(self, request, pk ):
         
         try:
          tipolote = TipoLote.objects.get(id=pk)  

         except LoteModel.DoesNotExist:
            
            return Response(f"Não encontrado.", status=status.HTTP_404_NOT_FOUND)

         serializer = self.serializer_class(tipolote, data=request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(f"Informacoes actualizadas com sucesso!", status=status.HTTP_200_OK)
         
         else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            tipolote = TipoLote.objects.get(id=pk)
        
        except TipoLote.DoesNotExist:
            return Response("Nao Encontrado", status=status.HTTP_404_NOT_FOUND)
        
        tipolote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DescricaoCreateListView(generics.ListCreateAPIView):

    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = Descricaomodel.objects.all()
    serializer_class = DescricaoSerializer


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
    queryset = Descricaomodel.objects.all()
    serializer_class = DescricaoSerializer

    def put(self, request, pk ):
         
         try:
          descricao = Descricaomodel.objects.get(id=pk)  

         except Descricaomodel.DoesNotExist:
            
            return Response(f"Não encontrado.", status=status.HTTP_404_NOT_FOUND)

         serializer = self.serializer_class(descricao, data=request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(f"Informacoes actualizadas com sucesso!", status=status.HTTP_200_OK)
         
         else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
         
    def delete(self, request, pk):
        try:
            descricao = Descricaomodel.objects.get(id=pk)
        
        except TipoLote.DoesNotExist:
            return Response("Nao Encontrado", status=status.HTTP_404_NOT_FOUND)
        
        descricao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DetalhesCreateListView(generics.ListCreateAPIView):

    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = DetalhesModel.objects.all()
    serializer_class = DetalhesSerializer


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



class DetalhesUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = DetalhesModel.objects.all()
    serializer_class = DetalhesSerializer

    def put(self, request, pk ):
         
         try:
          descricao = DetalhesModel.objects.get(id=pk)  

         except DetalhesModel.DoesNotExist:
            
            return Response(f"Não encontrado.", status=status.HTTP_404_NOT_FOUND)

         serializer = self.serializer_class(descricao, data=request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(f"Informacoes actualizadas com sucesso!", status=status.HTTP_200_OK)
         
         else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
         
    def delete(self, request, pk):
        try:
            descricao = Descricaomodel.objects.get(id=pk)
        
        except TipoLote.DoesNotExist:
            return Response("Nao Encontrado", status=status.HTTP_404_NOT_FOUND)
        
        descricao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class LocalizacaoLoteView(generics.ListCreateAPIView):
    queryset = LocalizacaoLoteModel.objects.all()
    serializer_class = LocalizacaoLoteSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    def get(self, request ):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        serializer = self.serializer_class(self.queryset[start_num:end_num] , many=True)
        return Response({
            "points": serializer.data
        })
    def post(self, request, *args, **kwargs):
        try:
            if not request.user.is_staff:
                return Response("Você deve ter permissões de administrador.", status=status.HTTP_401_UNAUTHORIZED)
            print(request.data)
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():

                serializer.save()
                print(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class LocalizacaoLoteretrieveView(generics.RetrieveAPIView):
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    queryset = LocalizacaoLoteModel.objects.all()
    serializer_class = LocalizacaoLoteSerializer

    def retrieve(self, request, *args, pk):
        try:
            localizacao = self.queryset.get(id=pk)
            serializer = self.serializer_class(localizacao)

            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
        except LoteModel.DoesNotExist:
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


    def put(self, request, pk):
        try:
            localizacao = LocalizacaoLoteModel.objects.get(id=pk)

        except LocalizacaoLoteModel.DoesNotExist:
                return Response("Localizacao nao encontrada", status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(localizacao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Informacoes Actualizadas com sucesso!", status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, pk):
        try:
            localizacao = LocalizacaoLoteModel.objects.get(id=pk)
        
        except LocalizacaoLoteModel.DoesNotExist:
                return Response("Localizacao nao encontrada", status=status.HTTP_404_NOT_FOUND)
        
        localizacao.delete()
        return Response("Eliminado Com Sucesso", status=status.HTTP_204_NO_CONTENT)


class LoteSolicitacaoListView(generics.ListAPIView):
    queryset = LoteSolicitacaoModel.objects.all()
    serializer_class = LoteSolicitacaoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [JWTAuthentication]


    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()       
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except:
            return Response({"Sao necessarias credenciais de usario"}, status=status.HTTP_401_UNAUTHORIZED)


class LoteSolicitacaoRetrieveView(generics.RetrieveAPIView):
    queryset = LoteSolicitacaoModel.objects.all()
    serializer_class = LoteSolicitacaoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [JWTAuthentication]   

    def retrieve(self, request, *args, pk):
        try:
            lote = self.queryset.get(id=pk)
            serializer = self.serializer_class(lote)

            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
        except LoteModel.DoesNotExist:
            return Response({"message": "Solicitacao não encontrada."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class LoteSolicitacaoListCreate(generics.ListCreateAPIView):
    queryset = LoteSolicitacaoModel.objects.all()
    serializer_class = LoteSolicitacaoSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        try:

            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class LoteSolicitacaoDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoteSolicitacaoModel.objects.all()
    serializer_class = LoteSolicitacaoSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]

    def put(self, request, pk, *args):
        try:
               solicitacao = LoteSolicitacaoModel.objects.get(id=pk)

        except LoteSolicitacaoModel.DoesNotExist:
                return Response({"A solicitacao nao existe": solicitacao}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(solicitacao ,data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(f"Informacoes do lote n {solicitacao} actualizadas com sucesso!", status=status.HTTP_202_ACCEPTED)
        else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, reuqest, pk):
        try:
            solicitacao = LoteSolicitacaoModel.objects.get(id=pk)

        except LoteSolicitacaoModel.DoesNotExist:
            return Response({"Nao existe nenhuma solicitacao com o id :" : solicitacao}, status=status.HTTP_404_NOT_FOUND)


        solicitacao.delete()

        return Response(f"Solicitacao do lote com o {solicitacao.id}  eliminda com sucesso!")    



class FinalidadeListCrateView(generics.ListCreateAPIView):
    queryset = Finalidademodel.objects.all()
    serializer_class = FinalidadeSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]


    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()       
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({" Feito com sucesso"},status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"message": "Erro ao processar a solicitação.", "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class LoteAtribicaoListView(generics.ListAPIView):
    queryset = LoteAtribuicaoModel.objects.all()
    serializer_class = LoteAtribuicaoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes= [JWTAuthentication]

    def get(self, request):
        try:
            solicitacao = self.get_queryset()       
            serializer = self.serializer_class(solicitacao, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except:
            return Response({"Sao necessarias credenciais de usario"}, status=status.HTTP_401_UNAUTHORIZED)
        

class LoteAtribicaoListCreateView(generics.ListCreateAPIView):
    queryset = LoteAtribuicaoModel.objects.all()
    serializer_class = LoteAtribuicaoSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]

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

    def put(self, request, pk):
        try:
              atribuicao =LoteAtribuicaoModel.objects.get(id=pk)


        except LoteAtribuicaoModel.DoesNotExist:
                return Response(f"A atribuicao do lote com o id  nao existe" , status=status.HTTP_404_NOT_FOUND)
        

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
                return Response("Atribuicao do lote com o if  nao existe no sistema", status=status.HTTP_404_NOT_FOUND)
        
            atribuicao.delete()

            return Response("Solicitacao do lote com o id  eliminda com sucesso!", status=status.HTTP_204_NO_CONTENT)   



class HistoricoLoteListView(generics.ListAPIView):
    queryset = HistoricoLoteModel.objects.all()
    serializer_class = HistoricoLoteSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    def get(self, request): 
        try:
            historico = self.get_queryset()
            serializer = self.serializer_class(historico, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except :
                return Response({"Sao necessarias credenciais de usario!"}, status=status.HTTP_401_UNAUTHORIZED)




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
    


class DescricaoListView(generics.ListAPIView):
    queryset = Descricaomodel.objects.all()
    serializer_class = DescricaoSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]


class LoteEmpresaListCreate(generics.ListCreateAPIView):
    queryset = LoteEmpresaModel.objects.all()
    serializer_class = LoteEmpresaSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

class LoteEmpresaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoteEmpresaModel.objects.all()
    serializer_class = LoteEmpresaSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [JWTAuthentication]

