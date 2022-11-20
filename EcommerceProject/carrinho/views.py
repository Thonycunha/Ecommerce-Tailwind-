from django.shortcuts import render

from .carrinho import Carrinho

def add_to_carrinho(request, product_id):
    carrinho = Carrinho(request)
    carrinho.add(product_id)

    return render(request, 'carrinho/menu_carrinho.html')
