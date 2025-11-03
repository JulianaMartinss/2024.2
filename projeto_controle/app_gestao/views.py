from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def listar_colaboradores(request: HttpRequest):
    return render(request, 'app_gestao/pages/listar_colaboradores.html')

def remover_colaboradores(request: HttpRequest):
    raise NotImplementedError

def cadastrar_colaboradores(request: HttpRequest):
    raise NotImplementedError

def editar_colaboradores(request: HttpRequest):
    raise NotImplementedError