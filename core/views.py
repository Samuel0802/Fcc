from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def ramal(request, ramal_id):

    return render(request, 'ramal.html', {'ramal_id': ramal_id})

def coorporativo(request, coorporativo_id):

    return render(request, 'coorporativo.html', {'coorporativo_id': coorporativo_id})

def justificativa(request, justificativa_id):

    return render(request, 'justificativa.html', {'justificativa_id': justificativa_id})

def voltar_para_tela_inicial(request):
    # Redireciona para a página inicial (rota 'index')
    return render(request, 'index.html')
