from rest_framework import serializers
from .models import pagamento_atribuicao

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pagamento_atribuicao
        fields ="__all__"