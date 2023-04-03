from django.urls import path
from . import views

urlpatterns = [

    path('',views.index),
    path('inicio/',views.index),
    path('login/', views.loginFormUser),
    path('loginAdm/', views.loginFormAdm),
    path('loginEmp/', views.loginFormEmp),
    path('register/', views.registerForm),
    path('delete_user/<int:id>/',views.delete_user),
    path('delete_emp/<int:id>',views.delete_emp)

]
