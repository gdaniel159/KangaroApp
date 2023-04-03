from django import forms
from .models import Empresa,Usuario
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    usuario = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterFormUser(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.initial['id_estatusUs'] = 1

    class Meta:

        model = Usuario
        fields = ('id_estatusUs','id_categoria_profesional','nombresUs','correoUs','dniUs','sexoUs','userUs','passwordUs')

class RegisterFormEmp(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.initial['id_estatusEmp'] = 3

    class Meta:

        model = Empresa
        fields = ('id_estatusEmp','id_tipo_empresa','nombreEmp','correoEmp','rucEmp','userEmp','passwordEmp','url_sitioEmp')