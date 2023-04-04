from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='inicio'),
    path('inicio/',views.index,name='inicio_url'),
    path('login/',views.loginForm,name='login_usuarios'),
    path('register/', views.registerForm, name='register_usuarios'),
    # Se debe arreglar eso de que al acceder a esa ruta no se pueda acceder a esto mismo
    path('intranet/',views.intranet,name='intranet'),
    path('registro_empresa/',views.registerEmpresarial, name='registro_empresa'),
    
    path('delete_user/<int:id>/',views.delete_user),
    path('delete_emp/<int:id>',views.delete_emp)

]
