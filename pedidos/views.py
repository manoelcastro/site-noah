from django.shortcuts import render
from .models import Pessoa

def client_list(request):
    clientes = Pessoa.objects.all()
    return render(request, 'pedidos/client_list.html', {'clientes': clientes})
    
