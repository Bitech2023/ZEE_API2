from django.db import models
from lotes.models import LoteModel
from utils.defaultModel import globalModel

class Descricaomodel(globalModel):
    descricao = models.TextField()
    detalhes = models.TextField()
    loteId = models.ForeignKey(LoteModel, on_delete=models.CASCADE)

