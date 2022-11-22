from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .carrinho import Carrinho

def add_to_carrinho(request, product_id):
    carrinho = Carrinho(request)
    carrinho.add(product_id)

    return render(request, 'carrinho/menu_carrinho.html')

def carrinho(request):
    return render(request, 'carrinho/carrinho.html')

@login_required
def retirada(request):
    return render(request, 'carrinho/retirada.html')