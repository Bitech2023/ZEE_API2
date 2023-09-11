from django.db import models
from empresas.models import EmpresaModel
from utils.defaultModel import globalModel


class TipoModel(globalModel):
     titulo = models.CharField(max_length=125)
     descricao = models.TextField()


     def __str__(self):
          return self.titulo

class InfraestruturaModel(globalModel):
     informacao = models.TextField()


class Loteimage(globalModel):
    titulo = models.CharField(max_length=125)
    loteId = models.ForeignKey("LoteModel", on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='imagems/lote/', null=True)

    def __str__(self) -> str:
         return self.titulo



class LoteModel(globalModel):
         
     option_estado = [
     ('desocupado','Desocupado'),
     ('ocupado','Ocupado'),
     ('em desenvolvimento', 'Em Deselvovimento')
     ]   

     identificadordolote = models.CharField(max_length=125, null=False, unique=True)
     status = models.CharField( choices=option_estado, default= 'desocupado', max_length=25)
     data_disponibilidade = models.DateField(auto_now_add=True) 
     comprimento = models.IntegerField(default=00000, null=False)
     largura = models.IntegerField(default=00000, null=False)
     imagem = models.ImageField(upload_to='imagens/lotes/',null=True)
     valor = models.DecimalField(decimal_places=2,max_digits=10, default=00000000)
     descricaolote = models.TextField(null=False)


     def __str__(self):
          return (f"{self.identificadordolote} - {self.status}")


class LoteDescricaoModel(globalModel):
     descricao = models.CharField(max_length=50)

     def __str__(self) -> str:
          return self.descricao


class LoteDetalheModel(globalModel):
     detalhe = models.CharField(max_length=125)
     descricao = models.ForeignKey("LoteDescricaoModel", on_delete=models.CASCADE) 
     loteid = models. ForeignKey("LoteModel", on_delete=models.CASCADE)
   

class LocalizacaoLoteModel(globalModel):
     longitude = models.CharField(max_length=35, null=True) 
     latitude = models.CharField(max_length=35, null=True)
     lote = models.ForeignKey("LoteModel", on_delete=models.CASCADE, null=True)


class GeoLocalizacaoModel(globalModel):
     longitude = models.CharField(max_length=35, null=True) 
     latitude = models.CharField(max_length=35, null=True)
     lote = models.ForeignKey("LoteModel", on_delete=models.CASCADE, null=True)


class LocalizacaoEmpresaModel(globalModel):
     longitude = models.CharField(max_length=35, null=True) 
     latitude = models.CharField(max_length=35, null=True)
     EmpresaModel = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE, null=True)


class LoteEmpresaModel(globalModel):
     loteId = models.ManyToManyField(LoteModel)
     empresaid = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE, default=True)


class FinalidadeSolicitacaoModel(globalModel):
     tipoId  = models.ForeignKey('TipoModel', on_delete=models.CASCADE)
     solicitacao = models.ForeignKey('LoteSolicitacaoModel', on_delete=models.CASCADE)


class Finalidademodel(globalModel):
     tipoId = models.ForeignKey("TipoModel", on_delete=models.CASCADE)
     loteid = models.ForeignKey("LoteModel", on_delete=models.CASCADE) 


class LoteSolicitacaoModel(globalModel):

     option_status = [
          ('pendente','Pendente'),
          ('negado','Negado'),
          ('aprovada','Aprovada')
     ]
     userId = models.ForeignKey("users.User",verbose_name="usuario", on_delete=models.CASCADE) 
     loteId = models.ForeignKey("LoteModel", verbose_name="identificadordolote" ,on_delete=models.CASCADE)
     data_solicitacao = models.DateField(auto_now_add=True)
     status = models.CharField(choices=option_status, default='Pendente', max_length=25)
     ano = models.IntegerField()
     mes = models.IntegerField()


# class DocumentosLottModel(globalModel):
#      titulo = models.CharField(max_length=125)
#      file = models.FileField(upload_to='documentos_necessarios/lote/') 
#      loteId = models.ForeignKey("LoteModel", on_delete=models.CASCADE)


class LoteAtribuicaoModel(globalModel):
     option_status = [
          ('pendente','Pendente'),
          ('negado','Negado'),
          ('aprovada','Aprovada')
     ]
     # loteId = models.ForeignKey(LoteModel, on_delete=models.CASCADE)
     # idEmpresa = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE)
     id_solicitacao = models.ForeignKey(LoteSolicitacaoModel, on_delete=models.CASCADE, null=True)
     data_tribuicao = models.DateField(auto_now_add=True)
     status = models.CharField(choices=option_status, max_length=25 )



class pagamento_atribuicao(globalModel):
     option_status = [
          ("pago","Pago"),
          ("pendente","Pendente"),
          ("cancelado","cancelado")
     ]
     atribuicao_id = models.ForeignKey(LoteAtribuicaoModel, on_delete=models.CASCADE)
     datapagamento = models.DateField(auto_now=True)
     valorpagamento = models.DecimalField(max_digits=10, decimal_places=2)
     numero_de_referencia = models.IntegerField()
     statuspagamento = models.CharField(choices=option_status,default="pendente", max_length=50) 


class HistoricoLoteModel(globalModel):
     idEmpresa = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE)
     loteId = models.ForeignKey(LoteModel, on_delete=models.CASCADE)
     descricao = models.TextField()
     data_atribuicao = models.DateField(auto_now_add=True)
     data_saida = models.DateField()


