from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .carrinho import Carrinho
from produtos.models import Produto
def add_to_carrinho(request, product_id):
    carrinho = Carrinho(request)
    carrinho.add(product_id)

    return render(request, 'carrinho/menu_carrinho.html')

def carrinho(request):
    return render(request, 'carrinho/carrinho.html')

def atualizar_carrinho(request, product_id, action):
    cart = Carrinho(request)

    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)

    Produtos = Produto.objects.get(pk=product_id)
    quantidade = cart.get_item(product_id)['quantity']

    item = {
        'produtos': {
            'id': Produtos.id,
            'nome': Produtos.name,
            'image': Produtos.image,
            'get_thumbnail': Produtos.get_thumbnail(),
            'valor': Produtos.price,
        },
        'total': quantidade * Produtos.price,
        'quantidade': quantidade,
    }

    response = render(request, 'carrinho/vitrine/item_carrinho.html',{'item': item})
    response['HX-Trigger'] = 'update-menu-carrinho'


    return response

@login_required
def retirada(request):
    return render(request, 'carrinho/retirada.html')

def hx_menu_carrinho(request):
    return render(request, 'carrinho/menu_carrinho.html')