from django.urls import path

from .views import index, ramal, coorporativo, voltar_para_tela_inicial, justificativa

urlpatterns = [
    path('', index, name='index'),
    path('ramal/<int:ramal_id>/', ramal, name='ramal'),
    path('coorporativo/<int:coorporativo_id>/', coorporativo, name='coorporativo'),
    path('justificativa/<int:justificativa_id>/', justificativa, name='justificativa_detalhes'),
    path('voltar/', voltar_para_tela_inicial, name='voltar'),

]
