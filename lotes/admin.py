from django.contrib import admin
from .models import *

admin.site.site_header = "ZEE+"
admin.site.site_title = "Gerenciador"
admin.site.index_title = "Zona Economica Especial de Luanda"
admin.site.site_url = "http://192.168.8.116:3000"
admin.site.name  = "ZEE"
admin.site.register(LoteModel)
admin.site.register(LocalizacaoLoteModel)
admin.site.register(LoteSolicitacaoModel)
admin.site.register(LoteAtribuicaoModel)
admin.site.register(HistoricoLoteModel)
admin.site.register(Descricaomodel)
admin.site.register(LoteEmpresaModel)
