from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializer import *


class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def elements(self, request, pk=None):
        queryset = Element.objects.filter(category_id=pk)
        serializer = ElementSerializer(queryset, many=True)
        return Response(serializer.data)


class TypesViewSet(viewsets.ModelViewSet):
    queryset = Types.objects.all()
    serializer_class = TypesSerializer

    @action(detail=True, methods=['get'])
    def elements(self, request, pk=None):
        queryset = Element.objects.filter(types_id=pk)
        serializer = ElementSerializer(queryset, many=True)
        return Response(serializer.data)
