from django.forms import ModelForm, Textarea, TextInput
from django import forms
from .models import Comment


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
    name = forms.CharField(label='Nombre', max_length=10, min_length=3)
    surname = forms.CharField(label='Apellido', max_length=10, min_length=3, required=False)
    phone = forms.RegexField(label='Teléfono', regex='\(\w{3}\)\w{3}-\w{4}', max_length=13, min_length=13)
    date_birth = forms.DateTimeField(label='Fecha de Nacimiento')