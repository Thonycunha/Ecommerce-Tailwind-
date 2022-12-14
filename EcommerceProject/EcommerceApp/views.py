from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import render, redirect

from produtos.models import Produto, Categoria

from .forms import EscreverForm

# Create your views here.
def home(request):
    Produtos = Produto.objects.all()[0:4]
    return render(request,'home/index.html',{'Produtos':Produtos})


def Cadastro(request):
    if request.method == 'POST':
        form = EscreverForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request,user)

            return redirect('/')

    else:
        form = EscreverForm()

    return render(request, 'home/cadastro.html',{'form': form})

def Login(request):
    return render(request, 'home/login.html')

def shop(request):
    Categorias = Categoria.objects.all()
    Produtos = Produto.objects.all()

    categorias_ativas = request.GET.get('Categorias','')

    if categorias_ativas:
        Produtos = Produtos.filter(categoria__slug=categorias_ativas)

    query = request.GET.get('query', '')

    if query:
        Produtos = Produtos.filter(Q(name__icontains=query) | Q(description__icontains=query))

    contexto = {
        'Categorias': Categorias,
        'Produtos':Produtos,
        'categorias_ativas': categorias_ativas
    }

    return render(request,'home/shop.html',contexto)
