from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_Name = 'Operacoes com Lotes'

urlpatterns =[
    path('index', Index.as_view(), name='index'),


    path('' , LoteListCreateView.as_view(), name = "Listar_os_Lotes_Existentes"),
    path('<uuid:pk>',LoteRetrieveUpdateDeleteView.as_view(), name ="Eliminar/actualizar_lote"),


    path('tipo', TipoLoteCreateListView.as_view()),
    path('tipo/<uuid:pk>', TipoUpdateDeleteView.as_view()),


    path('descricao', DescricaoCreateListView.as_view()),
    path('descricao/<uuid:pk>', descricaoUpdateDeleteView.as_view()),


    path('imagem', LoteImageListCreateView.as_view(), name="Lote_Image"),
    path('imagem/<uuid:pk>', LoteImagemRetrieveUpdateDestroy.as_view(),name="Lote_Imagem_delete"),


    path('detalhes', DetalhesCreateListView.as_view()),
    path('detalhes/<uuid:pk>', DetalhesUpdateDeleteView.as_view()),
    path('detalhes/lote/<uuid:pk>', DetalhesUpdateDeleteView.as_view()),


    path('localizacao', LocalizacaoLoteView.as_view(), name='Localizaao_do_lote'),
    path('localizacao/<uuid:pk>', LocalizacaoLoteUpdateDeleteView.as_view()),
    path('localizacao/lote/<str:pk>', LocalizacaoRetrieveView.as_view()),


    path('geolocalizacao', GeoLocalizacaoLoteView.as_view(), name='Localizaao_do_lote'),
    path('geolocalizacao/<uuid:pk>', GeoLocalizacaoLoteUpdateDeleteView.as_view()),
    path('geolocalizacao/lote/<uuid:pk>', GeoLocalizacaoRetrieveView.as_view()),

    path('solicitacao', LoteSolicitacaoListCreateVier.as_view(), name="Lote_Solicitacao"),
    path('solicitacao/<uuid:pk>/', LoteSolicitacaoRetrievDeleteUpdateView.as_view(), name=""),
    path('solicitacao/lote', LoteSolicitacaoRetrieView.as_view()),


    path('solicitacao/finalidade', FinalidadeSolicitacaoListCrateView.as_view(), name="Lote_Solicitacao"),
    path('solicitacao/finalidade/<uuid:pk>/', FinalidadeSolicitacaoUpdateDeleteView.as_view(), name=""),
    path('solicitacao/finalidade/lote/<uuid:pk>', FinalidadeSolicitacaoRetrieveView.as_view()),


    path('atribuicao', LoteAtribicaoListCreateView.as_view(), name="Lote_Atribuicao"),
    path('atribuicao/<uuid:pk>/', LoteAtribuicaoUpdateDeleteView.as_view(), name="Actualizar/Eliminar_Lote"),

    path('historico', HistoricoLoteListView.as_view(), name="Historico_List"),
    path('historico/create/', HistoricoLoteCreateView.as_view(), name="Historico_Create"),
    path('historico/update', HistoricoLoteUpdateDeleteView.as_view(), name="Historico_Update_Delete"),


    path('empresa', LoteEmpresaListCreate.as_view(), name="Lote_Empresa_Criar_listar"),
    path('empresa/update/<uuid:pk>', LoteEmpresaRetrieveUpdateDestroy.as_view(), name="Lote_Empresa_Actualizar_Destruir"),


    path("pagamentos",PagamentoListCreateView.as_view(), name="pagamento_Lista"),
    path('pagamentos/<uuid:pk>', PagamentoRetrieveUpdateDeleteView.as_view(), name="Pagamento_efectuar"),

    path("documento", DocumentoTituloListcreateView.as_view(), name="Documnetos_Tilulo"),
    path("documento/<uuid:pk>", DocumentoTitluoRetrieveDeleteUpdateView.as_view()),

    
    path("documento/lote", DocumentoLoteListcreateView.as_view(), name="Documnetos_Tilulo"),
    path("documento/lote/<uuid:pk>", DocumentoLoteRetrieveDeleteUpdateView.as_view()),

    path('geocode/', GeoCodeView.as_view(), name = "Obter a Distancia entre pontos"),

    path('template', template,name="Ola")
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
