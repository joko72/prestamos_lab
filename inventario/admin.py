from django.contrib import admin
from .models import Notebook
# Register your models here.
@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'marca', 'modelo', 'estado', 'disponible')
    search_fields = ('codigo', 'marca', 'modelo')
    list_filter = ('estado', 'disponible')