from django.db import models
from empresas.models import EmpresaModel
from utils.defaultModel import globalModel
from .models import LoteAtribuicaoModel
from lotes.models import *

class pagamento_atribuicao(globalModel):
     option_status = [
          ("pago","Pago"),
          ("pendente","Pendente"),
          ("cancelado","cancelado")
     ]
     atribuicao_id = models.ForeignKey(LoteAtribuicaoModel, on_delete=models.CASCADE)
     data_do_pagamento = models.DateField(auto_now=True)
     valor_do_pagamento = models.DateField(max_digits=10, decimal_places=2)
     numero_de_referencia = models.IntegerField()
     status_do_pagamento = models.CharField(choices=option_status,default="pendente", max_length=50) 
class LocalizacaoLoteModel(globalModel):
     latitude = models.CharField(max_length=9, null=True)
     longitude = models.CharField(max_length=9, null=True) 


class LoteModel(globalModel):
         
     option_estado = [
     ('desocupado','Desocupado'),
     ('ocupado','Ocupado'),
     ('em desenvolvimento', 'Em Deselvovimento')
     ]   
     numero_do_lote = models.IntegerField()
     status = models.CharField( choices=option_estado, default= 'desocupado', max_length=25)
     data_disponibilidade = models.DateField(auto_now_add=True) 
     Descricao =models.TextField(null=False) 
     tipo =models.CharField(max_length=50,  null=False) 
     comprimento = models.IntegerField(default=00000)
     largura = models.IntegerField(default=00000)
     localizacao =models.ForeignKey(LocalizacaoLoteModel, on_delete=models.CASCADE)
     imagem = models.ImageField(upload_to='static/images/lotes/', blank= True, null=True)
     valor_do_lote = models.DecimalField(decimal_places=2,max_digits=10, default=00000000)
     informacoes_de_infraestrutura = models.TextField()
     empresaID = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE, default=True)


     def __str__(self):
          return str(self.numero_do_lote)

class LoteSolicitacaoModel(globalModel):
     option_finalidade = [
          ('industrial','Industrial'),
          ('comercial','Comercial'),
          ('logistica e armazenamento','Logistica e Armazenamento'),
          ('tecnologia e inovação','Tecnologia e Inovação'),
          ('turismo e hospitalidade','Turismo e Hospitalidade'),
          ('energia','Energia'),
          ('agricultura e agroindústria','Agricultura e Agroindústria'),
          ('comércio internacional','Comércio Internacional'),
          ('indústria de pesca','Indústria de Pesca'),
          ('desenvolvimento imobiliário','Desenvolvimento Imobiliário')

     ]
     option_status = [
          ('em análise','Em Análise'),
          ('rejeitada','Rejeitada'),
          ('aprovada','Aprovada')
     ]
     nif_empresa_solicitante = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE) 
     data_solicitacao = models.DateField(auto_created=True)
     finalidade_de_utilizacao = models.CharField(choices=option_finalidade, default="Industrial",max_length=100)
     status_da_solicitacao = models.CharField(choices=option_status, default='Rejeitada', max_length=25)


class LoteAtribuicaoModel(globalModel):
     numero_lote = models.ForeignKey(LoteModel, on_delete=models.CASCADE)
     nif_empresa = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE)
     id_solicitacao = models.ForeignKey(LoteSolicitacaoModel, on_delete=models.CASCADE, null=True)
     data_de_atribuicao = models.DateField(auto_now_add=True)
     valor_da_atribuicao = models.DecimalField(max_digits= 10, decimal_places=2 ,default=0)
     duracao = models.CharField(max_length=10 , default='Em meses')


class HistoricoLoteModel(globalModel):
     nif_empresa = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE)
     numero_lote = models.ForeignKey(LoteModel, on_delete=models.CASCADE)
     descricao = models.TextField()
     data_atribuicao = models.DateField()
     data_saida = models.DateField()


class Descricaomodel(globalModel):
    descricao = models.TextField()
    detalhes = models.TextField()
    loteId = models.ForeignKey(LoteModel, on_delete=models.CASCADE)


      
