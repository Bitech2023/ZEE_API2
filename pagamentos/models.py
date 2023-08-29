from django.db import models
from utils.defaultModel import globalModel
from lotes.models import LoteAtribuicaoModel

class pagamento_atribuicao(globalModel):
    option_status =[
        ("pago","Pago"),
        ("pendente","Pendente"),
        ("cancelado","Cancelado")
    ]
    atribuicao_id = models.ForeignKey(LoteAtribuicaoModel, on_delete=models.CASCADE)
    data_do_pagamento = models.DateField(auto_now=True)
    valor_do_pagamento = models.DecimalField(max_digits=10, decimal_places=2)
    numero_de_referencia =models.IntegerField() 
    status_do_pagamento = models.CharField(choices=option_status, default="pendente", max_length=50)    



