from django.contrib import admin

from .models import *

# Register your models here.

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class ElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Types, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Element, ElementAdmin)