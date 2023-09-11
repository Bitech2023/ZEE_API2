from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_Name = 'Operacoes com Lotes'

urlpatterns =[
    path('', Index.as_view(), name='index'),


    path('lote' , LoteListCreateView.as_view(), name = "Listar_os_Lotes_Existentes"),
    path('lote/<uuid:pk>',LoteRetrieveUpdateDeleteView.as_view(), name ="Eliminar/actualizar_lote"),


    path('lote/tipo', TipoLoteCreateListView.as_view()),
    path('lote/tipo/<uuid:pk>', TipoUpdateDeleteView.as_view()),


    path('lote/descricao', DescricaoCreateListView.as_view()),
    path('lote/descricao/<uuid:pk>', descricaoUpdateDeleteView.as_view()),


    path('lote/imagem', LoteImageListCreateView.as_view()),
    path('lote/imagem/<uuid:pk>', LoteImagemRetrieveUpdateDestroy.as_view()),


    path('lote/detalhes', DetalhesCreateListView.as_view()),
    path('lote/detalhes/<uuid:pk>', DetalhesUpdateDeleteView.as_view()),
    path('lote/detalhes/lote/<uuid:pk>', DetalhesUpdateDeleteView.as_view()),


    path('lote/localizacao', LocalizacaoLoteView.as_view(), name='Localizaao_do_lote'),
    path('lote/localizacao/<uuid:pk>', LocalizacaoLoteUpdateDeleteView.as_view()),
    path('lote/localizacao/lote/<str:pk>', LocalizacaoRetrieveView.as_view()),


    path('lote/geolocalizacao', GeoLocalizacaoLoteView.as_view(), name='Localizaao_do_lote'),
    path('lote/geolocalizacao/<uuid:pk>', GeoLocalizacaoLoteUpdateDeleteView.as_view()),
    path('lote/geolocalizacao/lote/<uuid:pk>', GeoLocalizacaoRetrieveView.as_view()),

    path('lote/solicitacao', LoteSolicitacaoListCreateVier.as_view(), name="Lote_Solicitacao"),
    path('lote/solicitacao/<uuid:pk>/', LoteSolicitacaoRetrievDeleteUpdateView.as_view(), name=""),
    path('lote/solicitacao/lote/<uuid:pk>', LoteSolicitacaoRetrieView.as_view()),


    path('lote/solicitacao/finalidade', FinalidadeSolicitacaoListCrateView.as_view(), name="Lote_Solicitacao"),
    path('lote/solicitacao/finalidade/<uuid:pk>/', FinalidadeSolicitacaoUpdateDeleteView.as_view(), name=""),
    path('lote/solicitacao/finalidade/lote/<uuid:pk>', FinalidadeSolicitacaoRetrieveView.as_view()),


    path('lote/finalidade',FinalidadeListCrateView.as_view(), name="Criar Finalidade"),
    path('lote/finalidade/<uuid:pk>', FinalidadeRetrieveUpdateDeleteView.as_view()),
    path('lote/finalidade/lote/<uuid:pk>', FinalidadeRetrieveView.as_view()),


    path('lote/atribuicao', LoteAtribicaoListCreateView.as_view(), name="Lote_Atribuicao"),
    path('lote/atribuicao/<uuid:pk>/', LoteAtribuicaoUpdateDeleteView.as_view(), name="Actualizar/Eliminar_Lote"),

    path('lote/historico', HistoricoLoteListView.as_view(), name="Historico_List"),
    path('lote/historico/create/', HistoricoLoteCreateView.as_view(), name="Historico_Create"),
    path('lote/historico/update/<uuid:pk>/', HistoricoLoteUpdateDeleteView.as_view(), name="Historico_Update_Delete"),


    path('lote/empresa', LoteEmpresaListCreate.as_view(), name="Lote_Empresa_Criar_listar"),
    path('lote/empresa/update/<uuid:pk>', LoteEmpresaRetrieveUpdateDestroy.as_view(), name="Lote_Empresa_Actualizar_Destruir"),


    path("pagamentos",PagamentoListCreateView.as_view(), name="pagamento_Lista"),
    path('pagamentos/<uuid:pk>', PagamentoRetrieveUpdateDeleteView.as_view(), name="Pagamento_efectuar")
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)