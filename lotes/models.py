from django.db import models
from empresas.models import EmpresaModel
from utils.defaultModel import globalModel


class TipoLoteModel(globalModel):
     titulo = models.CharField(max_length=125)
     descricao = models.TextField()


     def __str__(self):
          return self.titulo

     class Meta:
         db_table = "TipoLote"
         verbose_name = "Tipo de Lote "
         verbose_name_plural = "Tipos de Lotes"
     
     
class InfraestruturaModel(globalModel):
     informacao = models.TextField()


class Loteimage(globalModel):
     titulo = models.CharField(max_length=125)
     lote = models.ForeignKey("lotes.LoteModel", on_delete=models.CASCADE)
     imagem = models.ImageField(upload_to='imagems/lotes/', null=True)


     def __str__(self):
          return f"{self.titulo}- {self.createdAt}" 
     
     
     class Meta:
         db_table = "LoteImagem"
         verbose_name = "Imagem de Lote "
         verbose_name_plural = "Imagens de Lotes"

     
class LoteModel(globalModel):
         
     option_estado = [
     ('desocupado','Desocupado'),
     ('ocupado','Ocupado'),
     ('em desenvolvimento', 'Em Deselvovimento')
     ]   

     codigoLote = models.CharField(max_length=125, null=True, blank=True)
     status = models.CharField( choices=option_estado, default= 'desocupado', max_length=25)
     data_disponibilidade = models.DateField(auto_now_add=True) 
     comprimento = models.IntegerField(default=00000, null=False)
     largura = models.IntegerField(default=00000, null=False)
     imagem = models.ImageField(upload_to='imagens/lotes/',null=True)
     valor = models.DecimalField(decimal_places=3,max_digits=12, default=00000000)
     descricaolote = models.TextField(null=False)


     def __str__(self):
          return (f"{self.codigoLote} - {self.status} - {self.createdAt}")
     
     class Meta:
         db_table = "Lotes"
         verbose_name = "Lote "
         verbose_name_plural = "Lotes"
     

class DocumentoTituloModel(globalModel):
     nome = models.CharField(max_length=50)

     def __str__(self )->str:
          return self.nome


class DocumentoLoteModel(globalModel):
     titulo = models.ForeignKey("lotes.DocumentoTituloModel", on_delete=models.CASCADE)
     documento = models.FileField(upload_to='documentos/pdf/', null=False)
     loteId = models.ForeignKey("lotes.LoteModel", on_delete=models.CASCADE)

     def __str__(self) -> str:
          return "Titlulo: {} - Lote: {}".format(self.titulo.nome, self.loteId.codigoLote)
     
     class Meta:
         db_table = "Documento_Lote"
         verbose_name = "Documento do Lote "
         verbose_name_plural = "Documentos do Lote"


class LoteDescricaoModel(globalModel):
     descricao = models.CharField(max_length=50)

     def __str__(self) -> str:

          return self.descricao
     
     class Meta:
          db_table = 'DescricaoLote'
          verbose_name = 'Descricao do lote'
          verbose_name_plural = 'Descricoes dos Lotes'


class LoteDetalheModel(globalModel):
     detalhe = models.CharField(max_length=125)
     descricao = models.ForeignKey("lotes.LoteDescricaoModel", on_delete=models.CASCADE) 
     loteid = models. ForeignKey("lotes.LoteModel", on_delete=models.CASCADE)
     
     def __str__(self) -> str:
          return self.detalhe
     
     class Meta:
          db_table = 'DetalheLote'
          verbose_name = 'Detalhe do lote'
          verbose_name_plural = 'Detalhes dos Lotes'

   
class LocalizacaoLoteModel(globalModel):
     longitude = models.CharField(max_length=35, null=True) 
     latitude = models.CharField(max_length=35, null=True)
     lote = models.ForeignKey("lotes.LoteModel", on_delete=models.CASCADE, null=True)

     def __str__(self) -> str:
          return "{} | {}".format(self.longitude,self.latitude)
     
     class Meta:
         db_table = "LocalizacaoLote"
         verbose_name = "Localizacao do Lote "
         verbose_name_plural = "Localizacoes dos Lotes"


class GeoLocalizacaoModel(globalModel):
     longitude = models.CharField(max_length=35, null=True) 
     latitude = models.CharField(max_length=35, null=True)
     lote = models.ForeignKey("lotes.LoteModel", on_delete=models.CASCADE, null=True)


     def __str__(self):
          return "Latutude:{} | Longitude{}".format(self.latitude,self.longitude)
     
     class Meta:
          db_table= "Geolocalizacao"
          verbose_name = "GeoLocalizacao"
          verbose_name_plural = "GeoLocalizacao"


class LocalizacaoEmpresaModel(globalModel):
     longitude = models.CharField(max_length=35, null=True) 
     latitude = models.CharField(max_length=35, null=True)
     EmpresaModel = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE, null=True)

     def __str__(self) -> str:
          return (f"{self.longitude} + {self.latitude}")


class LoteEmpresaModel(globalModel):
     loteId = models.ForeignKey("lotes.LoteModel", on_delete=models.CASCADE)
     # loteId = models.ManyToManyField(LoteModel)
     empresaId = models.ForeignKey("empresas.EmpresaModel", on_delete=models.CASCADE, default=True)

     def __str__(self):
          return ("{} - {}".format(self.empresaId.nome,self.loteId))
     
     class Meta:
          db_table = 'Lote_Empresa'
          verbose_name = 'Empresa'
          verbose_name_plural = 'Empresas'


class FinalidadeSolicitacaoModel(globalModel):
     tipoId  = models.ForeignKey(TipoLoteModel, on_delete=models.CASCADE)
     solicitacao = models.ForeignKey('lotes.LoteSolicitacaoModel', on_delete=models.CASCADE)


     def __str__(self):
          return "{} & {}".format(self.tipoId.titulo,self.solicitacao.loteId)
     
     class Meta:
         db_table = "FinalidadeLote "
         verbose_name = " Finalidade Lote "
         verbose_name_plural = "Finalidade Lote"


class LoteSolicitacaoModel(globalModel):

     option_status = [
          ('pendente','Pendente'),
          ('negado','Negado'),
          ('aprovada','Aprovada')
     ]

     userId = models.ForeignKey("users.User",verbose_name="usuario", on_delete=models.CASCADE) 
     loteId = models.ForeignKey("lotes.LoteModel", verbose_name="codigo Lote" ,on_delete=models.CASCADE)
     status = models.CharField(choices=option_status, default='Pendente', max_length=25)
     valor = models.DecimalField(max_digits=12, decimal_places=3)
     tempo = models.IntegerField(default=1, verbose_name="Tempo De Requisicao")


     def __str__(self) -> str:
          return (f"{self.loteId.codigoLote} - {self.status}")
     
     class Meta:
         db_table = "Solicitacao Lote"
         verbose_name = "Lote Solicitacao"
         verbose_name_plural = "Solicitacoes de Lotes"
     

class LoteAtribuicaoModel(globalModel):
     option_status = [
          ('pendente','Pendente'),
          ('negado','Negado'),
          ('aprovada','Aprovada')
     ]
     # loteId = models.ForeignKey("LoteModel", on_delete=models.CASCADE)
     # idEmpresa = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE)
     id_solicitacao = models.ForeignKey("lotes.LoteSolicitacaoModel", on_delete=models.CASCADE, null=True)
     data_tribuicao = models.DateField(auto_now_add=True)
     status = models.CharField(choices=option_status, max_length=25,default="aprovado")

     def __str__(self) -> str:
          return " {} - {}".format(self.id_solicitacao, self.status)
     
     class Meta:
         db_table = "AtribuicaoLote"
         verbose_name = "Atribuicao de Lote "
         verbose_name_plural = "Atribuicoes de Lotes"


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
     statuspagamento = models.CharField(choices=option_status,default="pago", max_length=50) 

     
class HistoricoLoteModel(globalModel):
     idEmpresa = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE)
     loteId = models.ForeignKey(LoteModel, on_delete=models.CASCADE)
     descricao = models.TextField()
     data_atribuicao = models.DateField(auto_now_add=True)
     data_saida = models.DateField()


