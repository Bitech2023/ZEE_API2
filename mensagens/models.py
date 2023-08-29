import datetime
from django.db import models
import empresas
from utils.defaultModel import globalModel
from empresas.models import EmpresaModel


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
    nif_empresa = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE)



# nova_notificacao = NotificacaoEmpresaModel(
#     titulo="Título da Notificação",
#     tipo_notificacao="Tipo da Notificação",
#     assunto_empresa="Conteúdo da Notificação",
#     data=datetime.date.today(),
#     prioridade="normal",
#     empresa_id=empresa
# )
# nova_notificacao.save()




