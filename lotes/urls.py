from django.urls import path
from .views import *

app_Name = 'Operacoes com Lotes'

urlpatterns =[
    path('', Index.as_view(), name='index'),
    path('lote/' , LoteListView.as_view(), name = "Listar_os_Lotes_Existentes"),
    path('lote/create/', LoteCreateView.as_view(), name = "Adicionar_novos_lotes"),
    path('lote/update/<uuid:pk>/',LoteUpdateDeleteView.as_view(), name ="Eliminar/actualizar_lote"),
    path('localizacao/', LocalizacaoLoteView.as_view(), name='Localizaao_do_lote'),
    path('lote/solicitacao/', LoteSolicitacaoListView.as_view(), name="Lote_Solicitacao"),
    path("lote/solicitacao/create/", LoteSolicitacaoListCreate.as_view(), name="Lote_Solicitacao"),
    path('lote/solicitacao/update/<uuid:pk>/', LoteSolicitacaoDeleteUpdateView.as_view(), name="Actualizar_Eliminar_Lote"),
    path('lote/atribuicao/', LoteAtribicaoListView.as_view(), name="Lote_Atribuicao"),
    path('lote/atribuicao/create/', LoteAtribicaoListCreateView.as_view(), name="Lotes_para_atribuicao"),
    path('lote/atribuicao/update/<uuid:pk>/', LoteAtribuicaoUpdateDeleteView.as_view(), name="Actualizar/Eliminar_Lote"),
    path('lote/historico/', HistoricoLoteListView.as_view(), name="Historico_List"),
    path('lote/historico/create/', HistoricoLoteCreateView.as_view(), name="Historico_Create"),
    path('lote/historico/update/<uuid:pk>/', HistoricoLoteUpdateDeleteView.as_view(), name="Historico_Update_Delete"),
    path('lote/descricao/', DescricaoListView.as_view(), name="Descricao_Lote" ),
    path('lote/empresa/', LoteEmpresaListCreate.as_view(), name="Lote_Empresa_Criar_listar"),
    path('lote/empresa/<uuid:pk>/', LoteEmpresaRetrieveUpdateDestroy.as_view(), name="Lote_Empresa_Actualizar_Destruir")
    ]