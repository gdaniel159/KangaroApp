from django.contrib import admin
from .models import Usuario,Administrador,Empresa,Status,CategoriaProfesional, TipoEmpresa

admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Empresa)
admin.site.register(Status)
admin.site.register(CategoriaProfesional)
admin.site.register(TipoEmpresa)

