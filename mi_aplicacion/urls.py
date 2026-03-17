from django.urls import path
from mi_aplicacion.views import Home,Escuelas,EscuelaAlta,EscuelaEditar,EscuelaEliminar,Maestros,MaestrosAlta,MaestrosEditar,MaestrosEliminar


urlpatterns = [
    path('',Home.as_view(), name="home"),
    path('escuelas/',Escuelas.as_view(), name="escuelas"),
    path('escuelas/alta',EscuelaAlta.as_view(), name="escuelas_alta"),
    path('escuelas/editar/<int:id>/',EscuelaEditar.as_view(), name="escuelas_editar"),
    path('escuelas/eliminar/<int:id>/',EscuelaEliminar.as_view(), name="escuelas_eliminar"),
    path('maestros/',Maestros.as_view(), name="maestros"),
    path('maestros/alta',MaestrosAlta.as_view(), name="maestros_alta"),
    path('maestros/editar/<int:id>/',MaestrosEditar.as_view(), name="maestros_editar"),
    path('maestros/eliminar/<int:id>/',MaestrosEliminar.as_view(), name="maestros_eliminar")
]