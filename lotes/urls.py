from django.urls import path
from .views import *

app_Name = 'Operacoes com Lotes'

urlpatterns =[
    path('', Index.as_view(), name='index'),
    path('lote' , LoteListView.as_view(), name = "Listar_os_Lotes_Existentes"),
    path('lote/create/', LoteCreateView.as_view(), name = "Adicionar_novos_lotes"),
    path('lote/update/<uuid:pk>',LoteUpdateDeleteView.as_view(), name ="Eliminar/actualizar_lote"),
    path('lote/<uuid:pk>', LoteRetrieveView.as_view(), name="Lote_List_one"),


    path('lote/tipo', TipoLoteCreateListView.as_view()),
    path('lote/tipo/<uuid:pk>', TipoLoteUpdateDelete.as_view()),

    path('lote/descricao', DescricaoCreateListView.as_view()),
    path('lote/descricao/<uuid:pk>', descricaoUpdateDeleteView.as_view()),
    
    path('lote/detalhes', DetalhesCreateListView.as_view()),
    path('lote/detalhe/<uuid:pk>', DetalhesUpdateDeleteView.as_view()),


    path('lote/localizacao', LocalizacaoLoteView.as_view(), name='Localizaao_do_lote'),
    path('lote/localizacao/update/<uuid:pk>', LocalizacaoLoteUpdateDeleteView.as_view()),
    path('lote/localizacao/<uuid:pk>', LocalizacaoLoteretrieveView.as_view()),

    path('lote/solicitacao', LoteSolicitacaoListView.as_view(), name="Lote_Solicitacao"),
    path("lote/solicitacao/create/", LoteSolicitacaoListCreate.as_view(), name="Lote_Solicitacao"),
    path('lote/solicitacao/update/<uuid:pk>/', LoteSolicitacaoDeleteUpdateView.as_view(), name="Actualizar_Eliminar_Lote"),
    path('lote/solicitacao/<uuid:pk>/', LoteSolicitacaoRetrieveView.as_view(), name=""),

    path('finalidade',FinalidadeListCrateView.as_view(), name="Criar Finalidade"),

    path('lote/atribuicao', LoteAtribicaoListView.as_view(), name="Lote_Atribuicao"),
    path('lote/atribuicao/create/', LoteAtribicaoListCreateView.as_view(), name="Lotes_para_atribuicao"),
    path('lote/atribuicao/update/<uuid:pk>/', LoteAtribuicaoUpdateDeleteView.as_view(), name="Actualizar/Eliminar_Lote"),

    path('lote/historico', HistoricoLoteListView.as_view(), name="Historico_List"),
    path('lote/historico/create/', HistoricoLoteCreateView.as_view(), name="Historico_Create"),
    path('lote/historico/update/<uuid:pk>/', HistoricoLoteUpdateDeleteView.as_view(), name="Historico_Update_Delete"),

    path('lote/descricao', DescricaoListView.as_view(), name="Descricao_Lote" ),

    path('lote/empresa', LoteEmpresaListCreate.as_view(), name="Lote_Empresa_Criar_listar"),
    path('lote/empresa/update/<uuid:pk>', LoteEmpresaRetrieveUpdateDestroy.as_view(), name="Lote_Empresa_Actualizar_Destruir"),


    path("pagamentos",LoteListView.as_view(), name="pagamento_Lista"),
    path('pagamentos/create/', LoteCreateView.as_view(), name="Pagamento_efectuar")
    ]