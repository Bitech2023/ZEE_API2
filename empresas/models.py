from django.db import models
from utils.defaultModel import globalModel


class EmpresaModel(globalModel):
    nome =  models.CharField(max_length=55, null=False)
    funcionarios =  models.IntegerField(null=True)
    nif = models.CharField(max_length=15, null=False)
    # dono = models.ForeignKey(DonoEmpresaModel, on_delete=models.CASCADE)
    logo  = models.ImageField(upload_to="static/imagens/logo/", blank= True, null=True)
    email = models.EmailField(unique=True)
    telefone = models.IntegerField(unique=True, default=927860898)
    detalhes = models.TextField()


    def __str__(self):
        return str(self.nif)
    

class SectorEmpresaModel(globalModel):
    actividade = models.CharField(max_length=125)

    def __str__(self):
        return self.actividade


class DocumentosModel(globalModel):
    descricao = models.CharField(max_length=55)
    
    def __str__(self):
        return str(self.descricao)

class DocumentosEmpresaModel(globalModel):
    documentos = models.ForeignKey(DocumentosModel, on_delete=models.CASCADE)
    empresa = models.ForeignKey(EmpresaModel, related_name='EmpresaModel', on_delete=models.CASCADE)
    caminho = models.FileField(upload_to='static/documentos/pdf/')
 

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
    empresa = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE)


    def __str__(self):  
        return self.bi


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

