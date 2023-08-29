from django.urls import path
from .views import *

app_Name = 'Operacoes com Lotes'

urlpatterns =[
    path('', Index.as_view(), name='index'),
    path('lote/list/' , LoteListView.as_view(), name = "Listar_os_Lotes_Existentes"),
    # path('lote/list/<uuid:pk>/' , LoteListView.as_view(), name = "Listar_Lote_Especifico"),
    path('lote/create/', LoteCreateView.as_view(), name = "Adicionar_novos_lotes"),
    path('lote/update/<uuid:pk>/',LoteUpdateDeleteView.as_view(), name ="Eliminar/actualizar_lote"),
    path('localizacao/', LocalizacaoLoteView.as_view(), name='Localizaao_do_lote'),
    path('lote/solicitacao/list/', LoteSolicitacaoListView.as_view(), name="Lote_Solicitacao"),
    path("lote/solicitacao/create/", LoteSolicitacaoListCreate.as_view(), name="Lote_Solicitacao"),
    path('lote/solicitacao/update/<uuid:pk>/', LoteSolicitacaoDeleteUpdateView.as_view(), name="Actualizar_Eliminar_Lote"),
    path('lote/atribuicao/list/', LoteAtribicaoListView.as_view(), name="Lote_Atribuicao"),
    path('lote/atribuicao/create/', LoteAtribicaoListCreateView.as_view(), name="Lotes_para_atribuicao"),
    path('lote/atribuicao/update/<uuid:pk>/', LoteAtribuicaoUpdateDeleteView.as_view(), name="Actualizar/Eliminar_Lote"),
    path('lote/historico/list/', HistoricoLoteListView.as_view(), name="Historico_List"),
    path('lote/historico/create/', HistoricoLoteCreateView.as_view(), name="Historico_Create"),
    path('lote/historico/update/<uuid:pk>/', HistoricoLoteUpdateDeleteView.as_view(), name="Historico_Update_Delete"),
    path('lote/descricao/list/', DescricaoListView.as_view(), name="Descricao_Lote" ),
    path("pagamentos/list/",LoteListView.as_view(), name="pagamento_Lista"),
    path('pagamentos/create/', LoteCreateView.as_view(), name="Pagamento_efectuar")
    ]