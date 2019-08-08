from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('sobre', views.sobre),
    path('login', views.login),
    path('cadastro', views.cadastro),
    path('cadastro_instituicao', views.cadastro_instituicao),
    path('perfil_paciente', views.perfil_paciente),
    path('perfil_instituicao', views.perfil_instituicao), 
    # Comentei pq quando eu fui rodar o projeto, a função ainda não tinha sido postada no repositório, então causava erro.
    # path('cadastro_cliente', views.cadastro_cliente)
]
