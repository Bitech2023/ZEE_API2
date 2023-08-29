from django.db import models
from utils.defaultModel import globalModel
import uuid


    
class FuncionariosModel(globalModel):

    option_sexo =[
        ("masculino","Masculino"),
        ("feminino","Feminino"),
        ("nao_binario","Nao_Binario")
    ]
    
    first_name = models.CharField(max_length=55 , default="Joao")
    last_name = models.CharField(max_length=55, default="Paulo")
    sexo = models.CharField(choices=option_sexo, default="Nao_binario", max_length=50)
    idade = models.PositiveSmallIntegerField()
    bi = models.CharField(max_length=15,null=False, unique=True)
    cargo = models.CharField(max_length=55, default="Cosinheiro",null=False)
    email = models.EmailField(unique=True)
    numero_telefone = models.IntegerField(unique=True, default=927860898,null=False)
    foto = models.ImageField(upload_to="static/imagens/fotos/", blank=True,null=True)


    def __str__(self):  
        return self.bi


class EmpresaModel(globalModel):
    nome_da_empresa =  models.CharField(max_length=55, null=False)
    numero_de_funcionarios =  models.IntegerField(null=True)
    principais_funcionarios = models.OneToOneField(FuncionariosModel, on_delete=models.CASCADE, max_length=100, default=0, null=True, unique=True)
    nif = models.CharField(max_length=15, null=False)
    dono_da_empresa = models.CharField(max_length=55 , null=False)
    sector_actividade =  models.CharField(max_length=55, null=False)
    logo  = models.ImageField(upload_to="static/imagens/logo/", blank= True, null=True)
    email_da_empresa = models.EmailField(unique=True)
    telefone = models.IntegerField(unique=True, default=927860898)
 

    def __str__(self):
        return str(self.nif)

 

class NotificacaoGeralModel(globalModel):
    option_prioridade =[
        ("baixa","Baixa"),
        ("normal","Normal"),
        ("alta","Alta")
]

    titulo = models.CharField(max_length=50)
    tipo_notificacao = models.CharField(max_length=50)
    assunto = models.TextField(default="")
    data = models.DateField(default=0)
    prioridade = models.CharField(choices=option_prioridade, default="", max_length=50)
    nif_empresa = models.ManyToManyField(EmpresaModel)


class NotificacaoEmpresaModel(globalModel):
    option_prioridade =[
        ("baixa","Baixa"),
        ("normal","Normal"),
        ("alta","Alta")
]
    titulo = models.CharField(max_length=50)
    tipo_notificacao = models.CharField(max_length=50)
    assunto_empresa = models.TextField(default="")
    data = models.DateField(default=0)
    prioridade = models.CharField(choices=option_prioridade, default="", max_length=50)
    nif_empresa = models.OneToOneField(EmpresaModel, on_delete=models.CASCADE)

