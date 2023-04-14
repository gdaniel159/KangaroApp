from django import forms
from .models import Empresa,Usuario,Curriculum, ExperienciaLaboral, FormacionAcademica, Post, PostDetalle, Ayuda

class LoginForm(forms.Form):

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    usuario = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    account_type = forms.ChoiceField(choices=[('user', 'User'), ('admin', 'Admin'), ('company', 'Company')])


class RegisterFormUser(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.initial['id_estatusUs'] = 1

    class Meta:

        model = Usuario
        fields = ('id_estatusUs','id_categoria_profesional','nombresUs','correoUs','dniUs','sexoUs','telefono','direccion','userUs','passwordUs','profileUser')

class RegisterFormEmp(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.initial['id_estatusEmp'] = 3

    class Meta:

        model = Empresa
        fields = ('id_estatusEmp','id_tipo_empresa','nombreEmp','correoEmp','rucEmp','userEmp','passwordEmp','url_sitioEmp','profileEmp')

class CurriculumForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            
            field.widget.attrs['class'] = 'form-control'

    class Meta:
    
        model = Curriculum
        fields = ('perfil_profesional','idiomas','conocimientos','habilidades')

class ExperienciaLaboralForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
    
        model = ExperienciaLaboral
        fields = ('nombre_empresa','cargo_ocupado','tarea_realizadas','inicio','fin')

class FormacionAcademicaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
    
        model = FormacionAcademica
        fields = ('nombreInstitucion','grado_titulo','carrera','inicio','fin')

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            
            field.widget.attrs['class'] = 'form-control'

    class Meta:
    
        model = Post
        fields = ('requerimientos',)

class PostDetalleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

            super().__init__(*args, **kwargs)

            for field_name, field in self.fields.items():
                
                field.widget.attrs['class'] = 'form-control'

    class Meta:
    
        model = PostDetalle
        fields = ('titulo','descripcion')

class AyudaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

            super().__init__(*args, **kwargs)

            for field_name, field in self.fields.items():
                
                field.widget.attrs['class'] = 'form-control'

    class Meta:
    
        model = Ayuda
        fields = ('nombre_persona','telefono','correo','problema')