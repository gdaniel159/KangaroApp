from django.contrib import admin
from .models import Usuario,Administrador,Empresa,Status,CategoriaProfesional, TipoEmpresa,Post,PostDetalle,Solicitud,FormacionAcademica,Curriculum,ExperienciaLaboral,Ayuda

admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Empresa)
admin.site.register(Status)
admin.site.register(CategoriaProfesional)
admin.site.register(TipoEmpresa)
admin.site.register(Post)
admin.site.register(PostDetalle)
admin.site.register(Solicitud)
admin.site.register(Curriculum)
admin.site.register(FormacionAcademica)
admin.site.register(ExperienciaLaboral)
admin.site.register(Ayuda)

