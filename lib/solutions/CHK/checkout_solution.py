

class Sku:
    def __init__(self, price, offer_unit=None, offer_price=None):
        self.price = price
        self.offer_unit=offer_unit
        self.offer_price=offer_price

    def calculate_price(self,amount):
        if self.offer_unit and self.offer_price:
            return amount // self.offer_unit * 
        else:
            return amount * self.price

prices = {
    'A': {'price': 50, 'offer_unit': 3, 'offer_price': 130},
    'B': {'price': 30, 'offer_unit': 2, 'offer_price': 45},
    'C': {'price': 20},
    'D': {'price': 15},
}

special_offers = {
    'A': (3, 130),
    'B': (2, 45),
}
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):


def calculate_price_for_item(item, price, offer_unit, offer_price):

