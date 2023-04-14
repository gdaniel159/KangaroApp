from django.shortcuts import  render, redirect
from .forms import LoginForm, RegisterFormUser, RegisterFormEmp, ExperienciaLaboralForm, FormacionAcademicaForm,CurriculumForm,PostForm,PostDetalleForm, AyudaForm
from .models import Usuario, Empresa, Administrador, Post, PostDetalle,Curriculum,FormacionAcademica, ExperienciaLaboral,Solicitud, Ayuda
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from urllib.parse import urlencode
from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone
from django.template.loader import get_template

# Paginas estaticas con contenido predefinido

def index(request):

    return render(request,'index.html')

def ayuda(request):

    form = AyudaForm()

    if request.method == 'POST':

        form = AyudaForm(request.POST)

        if form.is_valid():

            nombre_persona = form.instance.nombre_persona
            telefono = form.instance.telefono
            correo = form.instance.correo
            problema = form.instance.problema

            email = 'kangaroservice29@gmail.com',

            data = form.save(commit=True)
            data.save()

            correo = EmailMultiAlternatives(f"Mensaje de problema enviador por {nombre_persona}",f'{nombre_persona} con el número de telefono {telefono} y el correo {correo} nos menciona que: \n {problema}','KANGARO COMPANY',email)

            correo.send()

            return redirect('inicio')
        
        else:

            return HttpResponse("Formulario mal enviado")   

    context = {

        'form':form

    }

    return render(request,'Ayuda.html',context)

def contacto(request):

    return render(request,'Contactanos.html')

def terminos(request):

    return render(request,'tyc.html')

def perfiles(request,id):

    user = Usuario.objects.get(id_usuario=id)

    curriculum = Curriculum.objects.get(id_usuario=id)

    formacion = FormacionAcademica.objects.filter(id_usuario=id)

    experiencia = ExperienciaLaboral.objects.filter(id_usuario=id)

    context = {

        'user':user,
        'currl':curriculum,
        'formacion':formacion,
        'experiencia':experiencia

    }

    return render(request,'perfil.html',context)

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
        # pds = Post.objects.filter(id_post=post.id_post)

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

    post = Post.objects.filter(id_post=id)
    
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

    empresa = post.empresa

    solicitudes = Solicitud.objects.filter(id_post=post)

    usuarios = Usuario.objects.filter(solicitud__in=solicitudes).distinct()

    formacion = FormacionAcademica.objects.filter(id_usuario__in=usuarios)

    context = {

        'solicitudes': solicitudes,
        'usuarios': usuarios,
        'formacion': formacion,
        'id_emp': empresa.id_empresa

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

def crear_curriculum(request,id):
    
    user = Usuario.objects.get(id_usuario=id)

    curriculum = Curriculum.objects.filter(id_usuario=user.id_usuario)

    form = CurriculumForm()

    if request.method == 'POST':

        form = CurriculumForm(request.POST)

        if form.is_valid():

            form.instance.id_usuario = Usuario.objects.get(id_usuario=id)

            data = form.save(commit=True)
            data.save()

            return redirect('curriculum',user.id_usuario)
        
        else:

            return HttpResponse("Registro Invalido")   

    context = {
        
        'users':user,
        'curriculum':curriculum,
        'form':form,

    }

    return render(request,'crear_cv.html',context)

# Añadir informacion academica al CV

def formacion_academica(request,id):

    user = Usuario.objects.get(id_usuario=id)

    form = FormacionAcademicaForm()

    formacion = FormacionAcademica.objects.filter(id_usuario=id)

    if request.method == 'POST':

        form = FormacionAcademicaForm(request.POST)

        if form.is_valid():

            form.instance.id_usuario = Usuario.objects.get(id_usuario=id)

            data = form.save(commit=True)
            data.save()

            return redirect('curriculum',user.id_usuario)
        
        else:

            return HttpResponse("Registro Invalido")   

    context = {

        'users':user,
        'form':form,
        'formaciones':formacion,

    }

    return render(request,'formacion_academica.html',context)

# Añadir experiencia laboral al CV

def experiencia_laboral(request,id):

    user = Usuario.objects.get(id_usuario=id)
    
    form = ExperienciaLaboralForm()

    experiencia = ExperienciaLaboral.objects.filter(id_usuario=id)

    if request.method == 'POST':

        form = ExperienciaLaboralForm(request.POST)

        if form.is_valid():

            form.instance.id_usuario = Usuario.objects.get(id_usuario=id)

            data = form.save(commit=True)
            data.save()

            return redirect('curriculum',user.id_usuario)
        
        else:

            return HttpResponse("Registro Invalido")   

    context = {

        'users':user,
        'form':form,
        'experiencias':experiencia

    }

    return render(request,'experiencia_laboral.html',context)

# Edicio de la experiencia laboral despues de hacer clic en el enlace

def edicion_experiencia(request,id):

    exp = ExperienciaLaboral.objects.get(id_experiencia=id)

    exp_data = ExperienciaLaboral.objects.get(id_experiencia=id)

    context = {

        'nemp':exp_data.nombre_empresa,
        'cargo':exp_data.cargo_ocupado,
        'tarea':exp_data.tarea_realizadas,
        'inicio':exp_data.inicio,
        'fin':exp_data.fin,
        'id_exp':exp_data.id_experiencia,
        'id_usuario':exp.id_usuario.id_usuario

    }

    return render(request,'edicion_experiencia.html',context)

def edicion_formacion(request,id):

    formacion = FormacionAcademica.objects.get(id_formacion=id)

    context = {

        'ninstitucion':formacion.nombreInstitucion,
        'grado':formacion.grado_titulo,
        'carrera':formacion.carrera,
        'inicio':formacion.inicio,
        'fin':formacion.fin,
        'id_for':formacion.id_formacion,
        'id_usuario':formacion.id_usuario.id_usuario

    }

    return render(request,'edicion_formacion.html',context)

# Actualizar curriculum

def actualizar_curriculum(request,id):

    objeto = get_object_or_404(Curriculum, id_curriculum = id)

    if request.method == 'POST':

        objeto.perfil_profesional = request.POST.get('perfil', '')
        objeto.idiomas = request.POST.get('idiomas', '')
        objeto.conocimientos = request.POST.get('conocimientos', '')
        objeto.habilidades = request.POST.get('habilidades', '')
        objeto.save()

        return redirect('curriculum',objeto.id_usuario.id_usuario)
    
def actualizar_formacion(request,id):

    objeto = get_object_or_404(FormacionAcademica, id_formacion = id)

    if request.method == 'POST':

        objeto.nombreInstitucion = request.POST.get('nombreInstitucion', '')
        objeto.grado_titulo = request.POST.get('grado', '')
        objeto.carrera = request.POST.get('carrera', '')
        objeto.inicio = request.POST.get('inicio', '')
        objeto.fin = request.POST.get('fin', '')
        objeto.save()

        return redirect('formacion',objeto.id_usuario.id_usuario)
    
def actualizar_experiencia(request,id):
    
    objeto = get_object_or_404(ExperienciaLaboral, id_experiencia = id)

    if request.method == 'POST':

        objeto.nombre_empresa = request.POST.get('nombreEmpresa', '')
        objeto.cargo_ocupado = request.POST.get('cargo', '')
        objeto.tarea_realizadas = request.POST.get('tarea', '')
        objeto.inicio = request.POST.get('inicio', '')
        objeto.fin = request.POST.get('fin', '')
        objeto.save()

        return redirect('experiencia',objeto.id_usuario.id_usuario)

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
                    return redirect('homepage_emp',id=emp_id)

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
        timestamp = timezone.now

        if form1.is_valid():

            nombreUs = form1.instance.nombresUs
            userUs = form1.instance.userUs
            dniUs = form1.instance.dniUs
            sexoUs = form1.instance.sexoUs
            correoUs = form1.instance.correoUs

            mailsend = get_template('Mensaje_RegisterUS.html')

            parametrosMail = mailsend.render({'NombresUs':nombreUs,'UserUs':userUs,'DniUs':dniUs,'SexoUs':sexoUs,'timestamp':timestamp})

            data = form1.save(commit=True)
            data.save()

            correo = EmailMultiAlternatives("Usted ya ha sido registrado!!",'','KANGARO CORP',[correoUs])
                
            correo.attach_alternative(parametrosMail, "text/html")
            correo.send()

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

            correoEmp = form.instance.correoEmp
            nombreEmp = form.instance.nombreEmp
            password = form.instance.passwordEmp
            rucEmp = form.instance.rucEmp
            userEmp = form.instance.userEmp
            timestamp = timezone.now

            mailsend = get_template('Mensaje_RegisterEMP.html')

            parametrosMail = mailsend.render({'NombreEMP':nombreEmp,'PasswordEmp':password,'RucEMP':rucEmp,'UserEMP':userEmp,'timestamp':timestamp})

            data = form.save(commit=True)
            data.save()

            correo = EmailMultiAlternatives("Su Empresa ya ha sido registrado!!",'','KANGARO CORP',[correoEmp])
                
            correo.attach_alternative(parametrosMail, "text/html")
            correo.send()

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

def realizar_post(request,id):

    emp = Empresa.objects.get(id_empresa=id)

    form = PostForm()

    if request.method == 'POST':

        form = PostForm(request.POST)

        if form.is_valid():

            form.instance.empresa = Empresa.objects.get(id_empresa=id)

            data = form.save(commit=True)
            data.save()

            return redirect('homepage_emp',emp.id_empresa)
        
        else:

            return HttpResponse("Registro Invalido")   
        
    context = {

        'form':form,
        'emp':emp

    }

    return render(request,'realizar_post.html',context)

def detalles_post(request,id):

    form = PostDetalleForm()
    post = Post.objects.get(id_post=id)

    if request.method == 'POST':

        form = PostDetalleForm(request.POST)

        if form.is_valid():

            form.instance.post = Post.objects.get(id_post=id)

            data = form.save(commit=True)
            data.save()

            return redirect('homepage_emp',post.empresa.id_empresa)
        
        else:

            return HttpResponse("Registro Invalido")   
        
    context = {

        'form':form,
        'id_emp':post.empresa

    }

    return render(request,'detalle_post.html',context)