from django.shortcuts import render

from .models import Comment
from .forms import CommentForm

# Create your views here.

def index(request):
    comments = Comment.objects.all()
    return render(request,'index.html', {'comments':comments})

def add(request):
    # si el metodo es Post
    if request.method == 'POST':
        # se crea el formulario 
        form = CommentForm(request.POST)
        # si el formulario es valido
        if form.is_valid():
            form.save()
    else:
        form = CommentForm()
    
    return render(request,'add.html', {'form':form})