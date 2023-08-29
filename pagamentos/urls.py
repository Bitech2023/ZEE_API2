from django.urls import path
from .views import *

app_name="Pagamentos"

urlpatterns = [
    path('pagamentos/list/', PagamentoListView.as_view(), name="Pagamento_Lista"),
    path('pagamentos/create/', PagamentoCreateView.as_view(), name="Pagamento_efectuar")
]