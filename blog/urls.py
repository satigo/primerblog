from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('publicacion/<int:pk>/', views.post_detail, name='post_detail'),
    path('publicacion/nueva', views.publicacion_nueva, name='publicacion_nueva'),
    path('publicacion/<int:pk>/editar/', views.publicacion_editar, name='publicacion_editar'),

]