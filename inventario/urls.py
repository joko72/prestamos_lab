from django.urls import path
from .views import (
    NotebookListView,
    NotebookCreateView,
    NotebookUpdateView,
    NotebookDeleteView,
    ReporteInternoView,
    AccesoDenegadoView,
)
urlpatterns = [
    path('', NotebookListView.as_view(), name='notebook_list'),
    path('nuevo/', NotebookCreateView.as_view(), name='notebook_create'),
    path('editar/<int:pk>/', NotebookUpdateView.as_view(), name='notebook_update'),
    path('eliminar/<int:pk>/', NotebookDeleteView.as_view(),name='notebook_delete'),
    path('reporte-interno/', ReporteInternoView.as_view(), name='reporte_interno'),
    path('acceso_denegado/', AccesoDenegadoView.as_view(), name='acceso_denegado'),
]
