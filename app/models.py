from django.db import models
from utils.defaultModel import globalModel
from django.utils import timezone


class Localizacao(globalModel):
     latitude = models.CharField(max_length=9, null=True)
     longitude = models.CharField(max_length=9, null=True)

     def __str__(self) :
          return self.latitude
     
     def __str__(self):
          return self.longitude
         

class Lote(globalModel):
     option_estado = [
     ('desocupado','Desocupado'),
     ('ocupado','Ocupado')
     ]   
 
     nome_lote = models.CharField(max_length=50,default="Nome")     
     Descricao =models.TextField(null=False) 
     area =models.IntegerField(  null=False)
     tipo =models.CharField(max_length=50,  null=False) 
     localizacaoid =models.ForeignKey(Localizacao, on_delete=models.CASCADE)
     observacao =models.TextField(null=False)
     valor = models.DecimalField(decimal_places=4,max_digits=8)
     estado =models.CharField(choices=option_estado, default= 'desocupado', max_length=25)

     def __str__(self) -> str:
          return self.nome_lote

class Impostos(globalModel):

     option_imposto = [
          ('mensal','Mensal'),
          ('trimestral','Trimestral'),
          ('anual','Anual')
     ]
     titulo = models.CharField(max_length=10)
     descricao = models.TextField(default="Aqui descreva o tipo de imposto a pagar")
     valor = models.DecimalField(max_digits=10,decimal_places=2)
     periodo =models.CharField(max_length=150, choices=option_imposto, default='mensal')




class Solicitacao(models.Model):
     option_solicitacao =[
          ('min','Min'),
          ('max','Max')
     ]
     Nome =models.CharField(max_length=50, null=False,blank=False)
     Sobre_nome=models.CharField(max_length=50,null=False,blank=False)
     email=models.EmailField(unique=True,null=False)
     telefone=models.IntegerField()
     observacao=models.TextField()
     orcamento=models.DecimalField(decimal_places=2,max_digits=4, choices=option_solicitacao, default='Min')


class NotificacaoGeral(models.Model):
     titulo=models.CharField(max_length=150,null=False,blank=False)
     descricao=models.TextField(default="DEscreva o genero da notificacao")
     data=models.DateTimeField(auto_now_add=True)


class Perfil(globalModel):

    
     nome_completo= models.CharField(max_length=150,null=False)
     username = models.CharField(max_length=50, null=False)
     descricao =models.TextField()
     nif = models.CharField(max_length=15)
     logo = models.ImageField(upload_to='static/images/Logo/', blank= True, null=True)
     documentos = models.PositiveSmallIntegerField()
     email = models.EmailField(unique=True,null=False)
     telefone =models.IntegerField() 
     password =models.CharField(max_length=25)
     

     def __str__(self) :
        return self.email


class ImpostoEmpresa(models.Model):
     option_imposto_empesa =[
          ('pago','Pago'),
          ('pendente','Pendente')
     ]
     empresa =  models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)
     imposto = models.ForeignKey(Impostos, on_delete=models.CASCADE, null=True)
     estado= models.CharField(max_length=100, choices=option_imposto_empesa, default='Pendente')


class NotificacaoEmpresa(models.Model):
     titulo=models.CharField(max_length=100,null=False)
     descricao=models.TextField(default="DEscreva o genero da notificacao")
     data=models.DateTimeField(auto_now_add=True)
     empresa  = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)


class HistoricoLote(globalModel):

     empresa  = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)
     descricao = models.TextField()
     data_atribuicao = models.DateTimeField(auto_now=True)
     data_de_saida =models.DateTimeField(auto_now_add=True)
     lote  = models.ForeignKey(Lote, on_delete=models.CASCADE, null=True)

     def __str__(self):
          return self.empresa



