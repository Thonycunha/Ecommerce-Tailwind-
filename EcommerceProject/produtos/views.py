from django.shortcuts import render

from .models import Produto

def produtos(request, slug):
    Produtos = Produto.objects.get(slug=slug)

    return render(request, 'produtos/produtos.html',{'Produtos': Produtos})