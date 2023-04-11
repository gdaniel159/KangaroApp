from django.shortcuts import  render, redirect
from .forms import LoginForm, RegisterFormUser, RegisterFormEmp, CurriculumForm,FormacionAcademicaForm, ExperienciaLaboralForm
from .models import Usuario, Empresa, Administrador, Post, PostDetalle,Curriculum,FormacionAcademica, ExperienciaLaboral,Solicitud
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from urllib.parse import urlencode
from django.shortcuts import render, get_object_or_404

# Paginas estaticas con contenido predefinido

def index(request):

    return render(request,'index.html')

def ayuda(request):

    return render(request,'Ayuda.html')

# Intranet del administador

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

# Home Page del usuario

def user_homepage(request,id):

    userMD = Usuario.objects.filter(id_usuario=id)
    pub_emp = Post.objects.all()
    pub_detalle = PostDetalle.objects.all()

    for post in pub_emp:
        post.empresa.image_url = post.empresa.profileEmp.url

    context = {

        'users':userMD,
        'pub_emp':pub_emp,
        'pub_detalle':pub_detalle

    }

    success_messages = messages.get_messages(request)
    success_messages_used = list(success_messages)
    context['success_messages'] = success_messages_used

    return render(request,'user_interface.html',context)

# Home page de la empresa

def emp_homepage(request,id):

    empMD = Empresa.objects.filter(id_empresa=id)
    pub_emp = Post.objects.filter(empresa=id)
    post = Post.objects.get(id_post=id)
    pub_detalle = PostDetalle.objects.filter(post__empresa__id_empresa=id)

    for post in pub_emp:
        post.empresa.image_url = post.empresa.profileEmp.url

    context = {

        'emps':empMD,
        'pub_emp':pub_emp,
        'pub_detalle':pub_detalle

    }

    return render(request,'empresa_interface.html',context)

# Vista para inspeccionar las solicitudes de interes de los usuario

def inspeccionar(request,id):

    post = Post.objects.get(id_post=id)

    solicitudes = Solicitud.objects.filter(id_post=post)

    usuarios = Usuario.objects.filter(solicitud__in=solicitudes).distinct()

    formacion = FormacionAcademica.objects.filter(id_usuario__in=usuarios)

    context = {

        'solicitudes': solicitudes,
        'usuarios': usuarios,
        'formacion': formacion

    }

    messages.success(request, '¡No hay datos dentro que mostrar!')

    return render(request, 'inspeccionar.html', context)

# Creacion del curriculum

def curriculum(request,id):

    user = Usuario.objects.filter(id_usuario=id)
    curriculum = Curriculum.objects.filter(id_usuario=id)
    formacion = FormacionAcademica.objects.filter(id_usuario=id)
    experiencia = ExperienciaLaboral.objects.filter(id_usuario=id)

    context = {

        'currl':curriculum,
        'users':user,
        'formaciones':formacion,
        'experiencias':experiencia

    }

    return render(request,'curriculum_model.html',context)

# Formulario para la creacion de un curriculum

def crear_curriculum(request,nombre):


    form = CurriculumForm()
    user = Usuario.objects.get(nombresUs=nombre)

    if request.method == 'POST':

        form = CurriculumForm(request.POST)

        if form.is_valid():

            data = form.save(commit=True)
            data.save()

            return redirect('crear_curriculum')
        else:

            return HttpResponse("Registro Invalido")  


    context = {

        'form':form,
        'users':user

    }

    return render(request,'crear_cv.html',context)

# Añadir informacion academica al CV

def formacion_academica(request,nombre):

    form = FormacionAcademicaForm()
    user = Usuario.objects.get(nombresUs=nombre)

    context = {

        'form':form,
        'users':user

    }

    return render(request,'formacion_academica.html',context)

# Añadir experiencia laboral al CV

def experiencia_laboral(request,nombre):

    form = ExperienciaLaboralForm()
    user = Usuario.objects.get(nombresUs=nombre)

    context = {

        'form':form,
        'users':user

    }

    return render(request,'experiencia_laboral.html',context)

# Formulario para el Login de usuarios (Administrativos - Usuarios - Empresas)

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

                    emp_id = emp.id_empresa
                    return redirect('homepage_emp',emp_id)

                else:

                    messages.error(request, "Invalid username or password.")
                    
            else:

                messages.error(request, "Invalid account type.")
    
    return render(request, 'login.html', {'form': form})

# Registro de Usuarios comunes

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

# Consultas delete para los usuario en el intranet

def delete_user(request,id):

    userDelete = Usuario.objects.get(id_usuario=id)
    userDelete.delete()
    return redirect('intranet')

def delete_emp(request,id):

    userEmp = Empresa.objects.get(id_empresa=id)
    userEmp.delete()
    return redirect('intranet')

# Register para los usuarios empresariales

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

# Seleccion de los usuarios empresariales y usuarios normales para su actualizacion de datos

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

# Consultas update

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

# Consulta para realizar la peticion de solicitud de un usuario

def solicitud(request,id_usuario,id_post):

    id_usuario = id_usuario
    id_post = id_post

    user = Usuario.objects.get(id_usuario=id_usuario)
    post = Post.objects.get(id_post=id_post)

    solicitud = Solicitud(id_usuario=user, id_post=post)

    solicitud.save()

    url = reverse('homepage_user', args=[user.id_usuario])

    messages.success(request, '¡Se envió el "Me Interesa" correctamente!')

    return redirect(url)