from django.urls import path
from . import views

urlpatterns = [

    path('',views.index),
    path('inicio/',views.index),
    path('login/',views.loginForm),
    path('register/', views.registerForm),
    # Se debe arreglar eso de que al acceder a esa ruta no se pueda acceder a esto mismo
    path('delete_user/<int:id>/',views.delete_user),
    path('delete_emp/<int:id>',views.delete_emp)

]
