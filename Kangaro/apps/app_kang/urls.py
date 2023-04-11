from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='inicio'),
    path('inicio/',views.index,name='inicio_url'),

    path('ayuda/',views.ayuda, name='ayuda'),

    path('login/',views.loginForm,name='login_usuarios'),
    path('register/', views.registerForm, name='register_usuarios'),
    path('registro_empresa/',views.registerEmpresarial, name='registro_empresa'),
    # Se debe arreglar eso de que al acceder a esa ruta no se pueda acceder a esto mismo
    path('intranet/',views.intranet,name='intranet'),
    path('homepage_user/<int:id>',views.user_homepage, name="homepage_user"),
    path('homepage_emp/<int:id>',views.emp_homepage,name="homepage_emp"),
    
    path('delete_user/<int:id>/',views.delete_user),
    path('delete_emp/<int:id>',views.delete_emp),

    path('editar_usuario/<int:id>',views.editar_usuario, name='editar_usuario'),
    path('editar_empresa/<int:id>',views.editar_empresa, name='editar_empresa'),
    
    path('actualizar_datos/<int:id>',views.actualizar_datos, name='actualizar_datos'),
    path('actualizar_datos_empresa/<int:id>',views.actualizar_datos_emp, name='actualizar_datos_empresa'),

    path('curriculum/<int:id>',views.curriculum, name='curriculum'),
    path('crear_curriculum/<str:nombre>', views.crear_curriculum, name="crear_curriculum"),

    path('formacion_academica/<str:nombre>',views.formacion_academica, name="formacion"),
    path('experiencia_laboral/<str:nombre>',views.experiencia_laboral, name="experiencia"),

    path('inspeccionar/<int:id>',views.inspeccionar,name="inspeccion"),
    path('enviar_solicitud/<int:id_usuario>/<int:id_post>',views.solicitud,name="solicitud")

]
