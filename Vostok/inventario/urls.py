from django.urls import path
from .views import crearInventarioView, agregar_material_inventario, ver_inventario, delete_inventario,\
    ver_inventario_material, eliminar_material_inventario, checklist, editar_material, editar_inventario

####### URLS US-04############


app_name = "inventario"
urlpatterns = [
    path('crear/', crearInventarioView, name='crear_inventario'),
    path('ver/', ver_inventario, name='ver_inventario'),
    path('<int:pk>/agregar_material/', agregar_material_inventario, name='agregar_material_inventario'),
    path('delete/<int:id>/', delete_inventario, name="delete_inventario"),
    path('<int:pk>/ver/material_inventario', ver_inventario_material, name='material_inventario'), ######## URLS US05 ########
    path('<int:inventario_id>/ver/material_inventario/<int:material_id>', eliminar_material_inventario, name='eliminar_material_inventario'),
    path('<int:pk>/json/', checklist, name='checklist'), #### URL US21 ####
    path('<int:inventario_id>/editar_material/<int:material_id>/', editar_material, name="editar_cantidad_material"), ######## US02 ########
    path('editar_inventario/<int:pk>/', editar_inventario, name="editar_inventario_view"), ######## US08 ########
]


####### URLS US-04############