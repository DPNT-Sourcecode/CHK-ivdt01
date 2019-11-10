

class Sku:
    def __init__(self, item, price, offer_unit=None, offer_price=None):
        self.item = item
        self.price = price
        self.offer_unit = offer_unit
        self.offer_price = offer_price

    def calculate_price(self,amount):
        sum = 0
        if self.offer_unit and self.offer_price:
            sum += amount // self.offer_unit * self.offer_price # in offer
            sum += amount %  self.offer_unit * self.price       # not in offer
        else:
            sum += amount * self.price
        return sum

store_skus = [
    Sku('A',50, 3, 130),
    Sku('B',30, 2, 45),
    Sku('C',20),
    Sku('D',15),
]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    for sku in store_skus:
        