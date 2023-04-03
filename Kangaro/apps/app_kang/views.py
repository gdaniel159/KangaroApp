from django.shortcuts import  render, redirect
from .forms import LoginForm, RegisterFormUser, RegisterFormEmp
from .models import Usuario, Empresa, Administrador
from django.http import HttpResponse, HttpResponseRedirect

def index(request):

    return render(request,'index.html')

def loginFormUser(request):

    form = LoginForm()

    # Retrive objects Usuario (user and password)

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            user = form.cleaned_data['usuario']
            password = form.cleaned_data['password']

            try:

                student = Usuario.objects.get(userUs=user,passwordUs=password)
                # admins = Administrador.objects.get(userAdm=user,passwordAdm=password)
                # company = Empresa.objects.get(userEmp=user,passwordEmp=password)

                return render(request,'paginas_inicio/bienvenida_usuario.html',{'student':student})
            
            except:

                return render(request,"login_error.html")

    context = {

        'form':form,

    }

    return render(request,'login.html',context)

def loginFormAdm(request):

    form = LoginForm()

    # Retrive objects Usuario (user and password)

    if request.method == 'POST':

        form = LoginForm(request.POST)

        userMD = Usuario.objects.all()
        empMD = Empresa.objects.all()



        if form.is_valid():

            user = form.cleaned_data['usuario']
            password = form.cleaned_data['password']

            try:

                # student = Usuario.objects.get(userUs=user,passwordUs=password)
                admins = Administrador.objects.get(userAdm=user,passwordAdm=password)
                # company = Empresa.objects.get(userEmp=user,passwordEmp=password)

                return render(request,'paginas_inicio/bienvenida_administrador.html',{'admin':admins,'user':userMD,'emp':empMD})
            
            except:

                return render(request,"login_error.html")

    context = {

        'form':form,

    }

    return render(request,'login.html',context)

def loginFormEmp(request):

    form = LoginForm()

    # Retrive objects Usuario (user and password)

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            user = form.cleaned_data['usuario']
            password = form.cleaned_data['password']

            try:

                # student = Usuario.objects.get(userUs=user,passwordUs=password)
                # admins = Administrador.objects.get(userAdm=user,passwordAdm=password)
                company = Empresa.objects.get(userEmp=user,passwordEmp=password)

                return render(request,'paginas_inicio/bienvenida_empresa.html',{'company':company})
            
            except:

                return render(request,"login_error.html")

    context = {

        'form':form,

    }

    return render(request,'login.html',context)

def registerForm(request):

    form1 = RegisterFormUser()
    form2 = RegisterFormEmp()

    if request.method == 'POST':

        form1 = RegisterFormUser(request.POST)
        form2 = RegisterFormEmp(request.POST)

        if form1.is_valid():

            data = form1.save(commit=True)
            data.save()

            return redirect('../login')

        elif form2.is_valid():

            data = form2.save(commit=True)
            data.save()

            return redirect('../loginEmp')

        else:

            return HttpResponse("Registro Invalido")      

    context = {

        'form1':form1,
        'form2':form2


    }

    return render(request,'register.html',context)

def delete_user(request,id):

    userDelete = Usuario.objects.get(id_usuario=id)
    userDelete.delete()
    # return redirect("paginas_inicio/bienvenida_administrador.html")
    return HttpResponse("Usuario eliminado")

def delete_emp(request,id):

    userEmp = Empresa.objects.get(id_empresa=id)
    userEmp.delete()
    return HttpResponse("Usuario eliminado")