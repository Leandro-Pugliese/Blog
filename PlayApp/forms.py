from datetime import datetime, time
from django import forms
from django.contrib.auth.forms import UserCreationForm
from PlayApp.models import Usuario
from PlayApp.models import Publicacion




class UsuarioForm(UserCreationForm):
    # nombre = forms.CharField(max_length=40, label="Nombre")
    # apellido = forms.CharField(max_length=40, label="Apellido")
    email = forms.EmailField(max_length=50, help_text="Agregar una dirección de Email válida")
    # tipo = forms.CharField()
    # password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    # password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ["username", "nombre", "apellido", "email", "tipo", "password1", "password2"]

class UsuarioUpdateForm(forms.ModelForm):
    # password = forms.CharField(label='Clave', widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = ("username", "nombre", "apellido", "email", "tipo")

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data ["username"]
            try:
                usuario = Usuario.objects.exclude(pk=self.instance.pk).get(username=username)
            except Usuario.DoesNotExist:
                return username
            raise forms.ValidationError('El nombre de Usuario "%s" ya esta en uso.' % usuario)
    


class PublicacionesForm(forms.ModelForm):
    fecha = forms.DateField(initial=datetime.now(), show_hidden_initial=True)
    
    
    class Meta:
        model = Publicacion
        fields = ("titulo","subtitulo", "noticia", "imagen")
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Titulo...'}),
            'subtitulo': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder':'Subtitulo...'}),
            'noticia': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'Noticia...'}),

        }

class UpdatePublicacionForm(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = ("titulo","subtitulo", "noticia", "imagen")
        

    def guardar(self, commit=True):
        publicacion = self.instance
        publicacion.titulo = self.cleaned_data['titulo']
        publicacion.subtitulo = self.cleaned_data['subtitulo']
        publicacion.noticia = self.cleaned_data['noticia']

        if self.cleaned_data['imagen']:
            publicacion.imagen = self.cleaned_data['imagen']
        if commit:
            publicacion.save()
        return publicacion



class ComentariosForm(forms.Form):
    nombre = forms.CharField()
    comentario = forms.CharField(widget=forms.Textarea())
    fecha = forms.DateField(initial=datetime.now(), show_hidden_initial=True)
   

