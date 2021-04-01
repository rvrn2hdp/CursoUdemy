from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import CommentForm, ContactForm
from django.core.exceptions import ValidationError

# Create your views here.


def index(request):
    comments = Comment.objects.all()
    return render(request, 'index.html', {'comments': comments})


def add(request):
    # si el metodo es Post
    if request.method == 'POST':
        # se crea el formulario
        form = CommentForm(request.POST)
        # si el formulario es valido
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CommentForm()

    return render(request, 'add.html', {'form': form})


def update(request, pk):

    com = get_object_or_404(Comment, pk=pk)
    # si el metodo es Post
    if request.method == 'POST':
        # se crea el formulario
        form = CommentForm(request.POST, instance=com)
        # si el formulario es valido
        if form.is_valid():
            form.save()
            return redirect('comment:update', pk=pk)
    else:
        form = CommentForm(instance=com)

    return render(request, 'update.html', {'form': form, 'com': com})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            contact = Contact()
            contact.name = form.cleaned_data['name']
            contact.surname = form.cleaned_data['surname']
            contact.phone = form.cleaned_data['phone']
            contact.email = form.cleaned_data['email']
            contact.date_birth = form.cleaned_data['date_birth']
            if 'document' in request.FILES:
                contact.document = request.FILES['document']
            contact.save()
            return redirect('comment:contact')
            print('Valido: '+ form.cleaned_data['sex'])
        else:
            print('Invalido')
            
    else:
        form = ContactForm()

    #if (form.errors):
    #    raise ValidationError(form.errors)

    return render(request, 'contact.html', {'form': form})
