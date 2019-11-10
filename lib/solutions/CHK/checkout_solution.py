import re
from collections import Counter


class Sku:
    def __init__(self, item, price, offer_unit=None, offer_price=None):
        self.item = item
        self.price = price
        self.offer_unit = offer_unit
        self.offer_price = offer_price

    def calculate_price(self, amount):
        sum = 0
        if self.offer_unit and self.offer_price:
            sum += amount // self.offer_unit * self.offer_price # in offers
            sum += amount %  self.offer_unit * self.price       # not in offers
        else:
            sum += amount * self.price
        return sum


store_skus = {
    'A': Sku('A', 50, 3, 130),
    'B': Sku('B', 30, 2, 45),
    'C': Sku('C', 20),
    'D': Sku('D', 15),
}


# skus = unicode string
def checkout(skus):
    # for any illegal input return -1
    if not re.search(r'[A-D]+', skus):
        return -1

    # get count of each item
    counts = Counter(skus)

    # calculate price
    sum = 0
    for item in counts:
        sum += store_skus[item].calculate_price(counts[item])
    return sum

