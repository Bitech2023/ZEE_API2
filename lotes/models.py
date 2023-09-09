from django.db import models
from empresas.models import EmpresaModel
from utils.defaultModel import globalModel


class TipoLote(globalModel):
     tipo = models.CharField(max_length=125)
     descricao = models.TextField()


     def __str__(self):
          return self.tipo


class InfraestruturaModel(globalModel):
     informacao = models.TextField()


class Loteimage(globalModel):
    nome = models.CharField(max_length=125)
    imagem = models.ImageField(upload_to='imagems/lote/')


class LoteModel(globalModel):
         
     option_estado = [
     ('desocupado','Desocupado'),
     ('ocupado','Ocupado'),
     ('em desenvolvimento', 'Em Deselvovimento')
     ]   

     identificadordolote = models.CharField(max_length=125, null=False, unique=True)
     status = models.CharField( choices=option_estado, default= 'desocupado', max_length=25)
     data_disponibilidade = models.DateField(auto_now_add=True) 
     # descricaolote = models.ForeignKey(Descricaomodel, on_delete=models.CASCADE) 
     tipolote = models.ForeignKey(TipoLote, on_delete=models.CASCADE, null=False)
     comprimento = models.IntegerField(default=00000, null=False)
     largura = models.IntegerField(default=00000, null=False)
     imagem = models.ImageField(upload_to='imagens/lotes/',null=True)
     # imagem = models.ForeignKey(Loteimage, on_delete=models.CASCADE)
     valor = models.DecimalField(decimal_places=2,max_digits=10, default=00000000)
     descricaolote = models.TextField(null=False)


     def __str__(self):
          return (f"{self.identificadordolote} - {self.status}")


class LocalizacaoLoteModel(globalModel):
     longitude = models.CharField(max_length=35, null=True) 
     latitude = models.CharField(max_length=35, null=True)
     lote = models.ForeignKey(LoteModel, on_delete=models.CASCADE, null=True)

class LocalizacaoEmpresaModel(globalModel):
     longitude = models.CharField(max_length=35, null=True) 
     latitude = models.CharField(max_length=35, null=True)
     EmpresaModel = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE, null=True)



class Descricaomodel(globalModel):
     descricao = models.CharField(max_length=125)


     def __str__(self):
         return self.descricao


class DetalhesModel(globalModel):
     detalhes = models.TextField()
     descricao = models.ForeignKey(Descricaomodel, on_delete=models.CASCADE)
     lote = models.ForeignKey(LoteModel, related_name='descricoes', on_delete=models.CASCADE)


     def __str__(self):
          return self.detalhes


class LoteEmpresaModel(globalModel):
     loteId = models.ManyToManyField(LoteModel)
     empresaid = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE, default=True)


class Finalidademodel(globalModel):
     finalidade = models.CharField(max_length=55)
     descricao = models.TextField()

     def __str__(self):
          return self.finalidade


class LoteSolicitacaoModel(globalModel):

     option_status = [
          ('em análise','Em Análise'),
          ('rejeitada','Rejeitada'),
          ('aprovada','Aprovada')
     ]
     nif_empresa_solicitante = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE) 
     data_solicitacao = models.DateField(auto_created=True)
     finalidade = models.ForeignKey(Finalidademodel, on_delete=models.CASCADE)
     status_da_solicitacao = models.CharField(choices=option_status, default='Em Análise', max_length=25)


class LoteAtribuicaoModel(globalModel):
     numero_lote = models.ForeignKey(LoteModel, on_delete=models.CASCADE)
     nif_empresa = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE)
     id_solicitacao = models.ForeignKey(LoteSolicitacaoModel, on_delete=models.CASCADE, null=True)
     datatribuicao = models.DateField(auto_now_add=True)
     valoratribuicao = models.DecimalField(max_digits= 10, decimal_places=2 ,default=0)
     duracao = models.CharField(max_length=10 , default='Em meses')


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
     nif_empresa = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE)
     numero_lote = models.ForeignKey(LoteModel, on_delete=models.CASCADE)
     descricao = models.TextField()
     data_atribuicao = models.DateField(auto_now_add=True)
     data_saida = models.DateField()


