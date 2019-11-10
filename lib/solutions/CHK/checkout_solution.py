import re
from collections import Counter


class Sku:
    def __init__(self, item, price, offer_unit=None, offer_price=None, extra_offer_unit=None, extra_offer_price=None):
        self.item = item
        self.price = price
        self.offer_unit = offer_unit
        self.offer_price = offer_price
        self.extra_offer_unit = extra_offer_unit
        self.extra_offer_price = extra_offer_price

    def calculate_price(self, amount):
        sum = 0

        if self.extra_offer_unit and self.extra_offer_price:
            in_extra_offer = amount // self.extra_offer_unit
            sum += in_extra_offer * self.extra_offer_price
            amount -= in_extra_offer

        if self.offer_unit and self.offer_price:
            in_offer = amount // self.offer_unit
            sum += in_offer * self.offer_price
            amount -= in_offer

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
    if not re.search(r'^[A-D]*$', skus):
        return -1

    # get count of each item
    item_counts = Counter(skus)

    # calculate total price
    total = 0
    for item in item_counts:
        total += store_skus[item].calculate_price(item_counts[item])
    return total

