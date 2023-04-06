from django.db import models

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
    
class Trabajo(models.Model):

    id_trabajo = models.BigAutoField(primary_key=True)
    id_empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    responsabilidades = models.CharField(max_length=100)
    beneficios = models.CharField(max_length=100)
    informacion_extra = models.CharField(max_length=100)

    def __str__(self):

        return self.titulo
    
class Solicitud(models.Model):

    id_solicitud = models.BigAutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    id_trabajo = models.ForeignKey(Trabajo,on_delete=models.CASCADE)