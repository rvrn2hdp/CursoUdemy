from django.forms import ModelForm, Textarea, TextInput
from django import forms
from .models import *
from django.core.validators import MinLengthValidator, EmailValidator

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'class': 'form-input'})
        }

    '''def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class':'form-input'})'''


class ContactForm(forms.Form):
    SEX = (
        (1, 'Masculino'),
        (2, 'Femenino'),
        (3, 'Otro'),
    )
    
    #name = forms.CharField(label='Nombre', validators=[MinLengthValidator(2, message='muy corto! (minimo %(limit_value)d) actual %(show_value)d ')])
    #name = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Nombre', max_length=10, min_length=3)
    name = forms.CharField(label='Nombre', max_length=10, min_length=3)
    email = forms.EmailField(label='Correo', initial='juan@gmail.com')
    surname = forms.CharField(label='Apellido',
                              max_length=10,
                              min_length=3,
                              required=False)
    phone = forms.RegexField(label='Teléfono',
                             regex='\(\w{3}\)\w{3}-\w{4}',
                             max_length=13,
                             min_length=13,
                             initial='(123)123-1234')
    date_birth = forms.DateTimeField(label='Fecha de Nacimiento', initial='2020-01-01')
    document = forms.FileField(label='Documento', required=False)
    terms = forms.BooleanField(label='Condiciones de servicios')
    #type_contact = forms.ChoiceField(label='Tipo de contacto', choices=CHOICE)
    type_contact = forms.ModelChoiceField(label='Tipo de Contacto', queryset=Typecontact.objects.all())
    sex = forms.ChoiceField(label='Sexo', choices=SEX)