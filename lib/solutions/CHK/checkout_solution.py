

class Sku:
    def __init__(self, price, offer_unit=None, offer_price=None):
        self.price = price
        self.offer_unit=offer_unit
        self.offer_price=offer_price

    def calculate_price(self,amount):
        sum = 0
        if self.offer_unit and self.offer_price:
            sum += amount // self.offer_unit * self.offer_price # offers
            sum += amount %  self.offer_unit * self.price       # non-offers
        else:
            sum += amount * self.price
        return sum

skus = {
    'A': Sku(50, 3, 130),
    'B': Sku(30, 2, 45),
    'C': Sku(20),
    'D': Sku(15),
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    