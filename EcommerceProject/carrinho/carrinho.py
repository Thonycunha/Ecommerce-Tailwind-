from django.conf import settings

from produtos.models import Produto

class Carrinho(object):
    def __init__(self,request) -> None:
        self.session = request.session
        carrinho = self.session.get(settings.CARRINHO_SESSION_ID)

        if not carrinho:
            carrinho = self.session[settings.CARRINHO_SESSION_ID] = {}

        self.carrinho = carrinho
            
    def __iter__(self):
        for p in self.carrinho.keys():
            self.carrinho[str(p)]['produtos'] = Produto.objects.get(pk=p)
    
    def __len__(self):
        return sum(item['quantity'] for item in self.carrinho.values())

    def save(self):
        self.session[settings.CARRINHO_SESSION_ID] = self.carrinho
        self.session.modified = True

    def add(self, product_id, quantity=1, update_quantity =False ):
        product_id = str(product_id)

        if product_id not in self.carrinho:
            self.carrinho[product_id] = {'quantity': 1, 'id': product_id}

        if update_quantity:
            self.carrinho[product_id]['quantity'] += int(quantity)

            if self.carrinho[product_id]['quantity'] == 0:
                self.remove(product_id)

        self.save()

    def remove(self,product_id):
        if product_id in self.carrinho:
            del self.carrinho[product_id]
            self.save()
