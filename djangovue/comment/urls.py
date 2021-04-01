from django.urls import path, include
from . import views

app_name = 'comment'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('contact/', views.contact, name='contact'),
    path('update/<int:pk>', views.update, name='update'),
]