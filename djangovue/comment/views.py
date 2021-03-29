from django.shortcuts import render, redirect, get_object_or_404

from .models import Comment
from .forms import CommentForm

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
            return redirect('update', pk=pk)
    else:
        form = CommentForm(instance=com)

    return render(request, 'update.html', {'form': form, 'com': com})

