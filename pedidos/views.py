from django.shortcuts import render

def client_list(request):
    return render(request, 'pedidos/client_list.html', {})
    
