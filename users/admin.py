from django.contrib import admin

from users.models import User, UserEmpresaModel, NivelModel

admin.site.register(User)
admin.site.register(UserEmpresaModel)
admin.site.register(NivelModel)