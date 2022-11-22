"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from django.conf.urls.static import static
from carrinho.views import add_to_carrinho, carrinho, retirada
from EcommerceApp.views import home,shop,Cadastro
from produtos.views import produtos


urlpatterns = [
    path('',home,name ='paginaInicial'),
    path('cadastro/',Cadastro, name='cadastro'),
    path('deslogar/', views.LogoutView.as_view(), name="deslogar"),
    path('login/',views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('shop/',shop,name ='shop'),
    path('shop/<slug:slug>/',produtos,name ='produtos'),
    path('carrinho/', carrinho, name='carrinho'),
    path('carrinho/retirada/', retirada, name='retirada'),
    path('add_to_carrinho/<int:product_id>', add_to_carrinho, name='add_to_carrinho'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
