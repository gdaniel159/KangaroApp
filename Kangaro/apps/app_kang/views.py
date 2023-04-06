from django.shortcuts import  render, redirect
from .forms import LoginForm, RegisterFormUser, RegisterFormEmp
from .models import Usuario, Empresa, Administrador
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from urllib.parse import urlencode
from django.shortcuts import render, get_object_or_404

def index(request):

    return render(request,'index.html')

def intranet(request):

    userMD = Usuario.objects.all()
    empMD = Empresa.objects.all()
    admin = request.GET.get('admin',None)

    context = {

        'user':userMD,
        'emp':empMD,
        'admin':admin

    }
    
    return render(request,'admin_iterface.html',context)

def user_homepage(request,id):

    userMD = Usuario.objects.filter(id_usuario=id)

    context = {

        'users':userMD,

    }

    return render(request,'user_interface.html',context)

def loginForm(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['usuario']
            password = form.cleaned_data['password']
            account_type = form.cleaned_data['account_type']
            
            user = None

            if account_type == 'user':

                user = Usuario.objects.filter(userUs=username, passwordUs=password).first()
                
                if user:

                    # return HttpResponse(user.nombresUs)
                    user_id = user.id_usuario
                    return redirect('homepage_user', id=user_id)
                
                else:

                    messages.error(request, "Invalid username or password.")
                    
            elif account_type == 'admin':

                admin = Administrador.objects.get(userAdm=username, passwordAdm=password)

                if admin:

                    url = reverse('intranet') + '?' + urlencode({'admin': admin.userAdm})
                    return redirect(url)

                else:

                    messages.error(request, "Invalid username or password.")
                    
            elif account_type == 'company':

                emp = Empresa.objects.filter(userEmp=username, passwordEmp=password).first()

                if emp:

                    return HttpResponse(emp.nombreEmp)

                else:

                    messages.error(request, "Invalid username or password.")
                    
            else:

                messages.error(request, "Invalid account type.")
    
    return render(request, 'login.html', {'form': form})

def registerForm(request):

    form1 = RegisterFormUser()

    if request.method == 'POST':

        form1 = RegisterFormUser(request.POST, request.FILES)

        if form1.is_valid():

            data = form1.save(commit=True)
            data.save()

            return redirect('../login')
        else:

            return HttpResponse("Registro Invalido")      

    context = {

        'form1':form1


    }

    return render(request,'register.html',context)

def delete_user(request,id):

    userDelete = Usuario.objects.get(id_usuario=id)
    userDelete.delete()
    return redirect('intranet')

def delete_emp(request,id):

    userEmp = Empresa.objects.get(id_empresa=id)
    userEmp.delete()
    return redirect('intranet')

def registerEmpresarial(request):

    form = RegisterFormEmp()

    if request.method == 'POST':

        form = RegisterFormEmp(request.POST, request.FILES)

        if form.is_valid():

            data = form.save(commit=True)
            data.save()

            return redirect('intranet')
        
        else:

            return HttpResponse("Registro Invalido")      

    admin = request.GET.get('admin',None)

    context = {

        'form':form,
        'admin':admin

    }

    return render(request,'crear_empresarial.html',context)

def editar_usuario(request,id):

    user = Usuario.objects.get(id_usuario=id)

    context = {

        'user':user

    }

    return render(request,'editar_usuario.html',context)

def editar_empresa(request,id):

    emp = Empresa.objects.get(id_empresa=id)

    context = {

        'emp':emp

    }

    return render(request,'editar_empresa.html',context)

def actualizar_datos(request,id):

    objeto = get_object_or_404(Usuario, id_usuario = id)

    if request.method == 'POST':

        objeto.nombresUs = request.POST.get('nombre', '')
        objeto.correoUs = request.POST.get('correo', '')
        objeto.dniUs = request.POST.get('dni', '')
        objeto.sexoUs = request.POST.get('sexo', '')
        objeto.userUs = request.POST.get('usuario', '')
        objeto.save()

        return redirect('intranet')
    
def actualizar_datos_emp(request,id):

    objeto = get_object_or_404(Empresa, id_empresa = id)

    if request.method == 'POST':

        objeto.nombreEmp = request.POST.get('nombre', '')
        objeto.correoEmp = request.POST.get('correo', '')
        objeto.rucEmp = request.POST.get('ruc', '')
        objeto.userEmp = request.POST.get('usuario', '')
        objeto.url_sitioEmp = request.POST.get('url', '')
        objeto.save()

        return redirect('intranet')