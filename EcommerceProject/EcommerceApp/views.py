import imp
from django.shortcuts import render

from produtos.models import Produto

# Create your views here.
def home(request):
    Produtos = Produto.objects.all()[0:4]
    return render(request,'home/index.html',{'Produtos':Produtos})

def shop(request):
    Produtos = Produto.objects.all()
    return render(request,'home/shop.html',{'Produtos':Produtos})
