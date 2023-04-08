from django.db import models

# Modelos para darle sentido a nuestro usuarios

class Status(models.Model):

    id_estatus = models.BigAutoField(primary_key=True)
    grado = models.CharField(max_length=50)

    def __str__(self):

        return self.grado
    
class CategoriaProfesional(models.Model):

    id_categoria_profesional = models.BigAutoField(primary_key=True)
    nombreCatPro = models.CharField(max_length=100)

    def __str__(self):

        return self.nombreCatPro
    
class TipoEmpresa(models.Model):

    id_tipo_empresa = models.BigAutoField(primary_key=True)
    nombreTipEmp = models.CharField(max_length=100)

    def __str__(self):

        return self.nombreTipEmp

# Usuarios Models

class Usuario(models.Model):
    
    id_usuario = models.BigAutoField(primary_key=True)
    id_estatusUs = models.ForeignKey(Status,on_delete=models.CASCADE)
    id_categoria_profesional = models.ForeignKey(CategoriaProfesional, on_delete=models.CASCADE)
    nombresUs = models.CharField(max_length=100)
    correoUs = models.EmailField(max_length=254)
    dniUs = models.CharField(max_length=8)
    sexoUs = models.CharField(max_length=1)
    userUs = models.CharField(max_length=100)
    passwordUs = models.CharField(max_length=50)
    profileUser = models.ImageField(upload_to='profiles',default='profiles/profileHitler.jpeg',blank=True)

    def __str__(self):

        return self.nombresUs
    
class Administrador(models.Model):
    
    id_administrador = models.BigAutoField(primary_key=True)
    id_estatusAdm = models.ForeignKey(Status,on_delete=models.CASCADE)
    nombresAdm = models.CharField(max_length=100)
    correoAdm = models.EmailField(max_length=254)
    dniAdm = models.CharField(max_length=8)
    sexoAdm = models.CharField(max_length=1)
    userAdm = models.CharField(max_length=100)
    passwordAdm = models.CharField(max_length=50)

    def __str__(self):

        return self.nombresAdm
    
class Empresa(models.Model):
    
    id_empresa = models.BigAutoField(primary_key=True)
    id_estatusEmp = models.ForeignKey(Status,on_delete=models.CASCADE)
    id_tipo_empresa = models.ForeignKey(TipoEmpresa,on_delete=models.CASCADE)
    nombreEmp = models.CharField(max_length=100)
    correoEmp = models.EmailField(max_length=254)
    rucEmp = models.CharField(max_length=11)
    userEmp = models.CharField(max_length=100)
    passwordEmp = models.CharField(max_length=50)
    url_sitioEmp = models.URLField(max_length=200)
    profileEmp = models.ImageField(upload_to='profiles',default='profiles/profileHitler.jpeg',blank=True)

    def __str__(self):

        return self.nombreEmp

# Post Models

class Post(models.Model):

    id_post = models.BigAutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    requerimientos = models.CharField(max_length=500)

    def __str__(self):
        return f"Post {self.id_post} - Creado el {self.fecha_creacion}"


class PostDetalle(models.Model):

    id_post_detalle = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

    def __str__(self):

        return f"{self.post}"

    
class Solicitud(models.Model):

    id_solicitud = models.BigAutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    id_post = models.ForeignKey(Post,on_delete=models.CASCADE)

# Curriculum Models

class Curriculum(models.Model):

    id_curriculum = models.BigAutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.id_usuario}"

class Habilidad(models.Model):

    id_habilidad = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):

        return f"{self.nombre}"

class Idioma(models.Model):

    id_idioma = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):

        return f"{self.nombre}"

class Formacion(models.Model):

    id_formacion = models.BigAutoField(primary_key=True)
    nombre_institucion = models.CharField(max_length=255)
    grado_titulo = models.CharField(max_length=255)
    carrera = models.CharField(max_length=255)
    inicio = models.DateField()
    fin = models.DateField()

    def __str__(self):

        return f"{self.carrera}"

class Conocimiento(models.Model):

    id_conocimiento = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):

        return f"{self.nombre}"

class CurriculumHabilidades(models.Model):

    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    habilidad = models.ForeignKey(Habilidad, on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.habilidad}"

class CurriculumIdiomas(models.Model):

    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.idioma}"

class CurriculumFormacionAcademica(models.Model):

    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    formacion = models.ForeignKey(Formacion, on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.formacion}"

class CurriculumConocimiento(models.Model):

    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    conocimiento = models.ForeignKey(Conocimiento, on_delete=models.CASCADE)

    def __str__(self):

        return f"{self.conocimiento}"