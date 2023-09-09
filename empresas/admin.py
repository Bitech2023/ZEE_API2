from django.contrib import admin
from . models import *

admin.site.register(EmpresaModel)
admin.site.register(FuncionariosModel)
admin.site.register(NotificacaoGeralModel)
admin.site.register(NotificacaoEmpresaModel)
admin.site.register(DocumentosModel)
admin.site.register(DocumentosEmpresaModel)
admin.site.register(SectorEmpresaModel)