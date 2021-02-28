from django.urls import path
from rest_framework import routers

from .viewsets import *

route = routers.SimpleRouter()
route.register('element', ElementViewSet)
route.register('category', CategoryViewSet)
route.register('types', TypesViewSet)

urlpatterns = route.urls
