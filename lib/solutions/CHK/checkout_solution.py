import re
from collections import Counter


class Sku:
    def __init__(self, item, price,
                 offer_unit=None, offer_price=None,
                 extra_offer_unit=None, extra_offer_price=None,
                 free_offer_unit=None, free_offer_item=None, ):
        self.item = item
        self.price = price
        self.offer_unit = offer_unit
        self.offer_price = offer_price
        self.extra_offer_unit = extra_offer_unit
        self.extra_offer_price = extra_offer_price
        self.free_offer_unit = free_offer_unit
        self.free_offer_item = free_offer_item

    def calculate_price(self, amount):
        sum = 0

        if self.extra_offer_unit and self.extra_offer_price:
            extra_offer_applies_count = amount // self.extra_offer_unit
            sum += extra_offer_applies_count * self.extra_offer_price
            amount -= extra_offer_applies_count * self.extra_offer_unit

        if self.offer_unit and self.offer_price:
            offer_applies_count = amount // self.offer_unit
            sum += offer_applies_count * self.offer_price
            amount -= offer_applies_count * self.offer_unit

        sum += amount * self.price
        return sum

    def apply_free_item_offer(self, basket_counts):
        if self.free_offer_unit and self.free_offer_item:
            if basket_counts.get(self.free_offer_item, 0) > 0:
                # reduce free item's count by the number of times we could apply the free item offer
                divider = self.free_offer_unit
                if self.free_offer_item == self.item:
                    divider += 1
                basket_counts[self.free_offer_item] -= basket_counts[self.item] // divider
                # ensure free item's count is not negative
                basket_counts[self.free_offer_item] = max(basket_counts[self.free_offer_item], 0)


store_skus = {
    'A': Sku('A', 50, offer_unit=3, offer_price=130, extra_offer_unit=5, extra_offer_price=200),
    'B': Sku('B', 30, offer_unit=2, offer_price=45),
    'C': Sku('C', 20),
    'D': Sku('D', 15),
    'E': Sku('E', 40, free_offer_unit=2, free_offer_item='B'),
    'F': Sku('F', 10, free_offer_unit=2, free_offer_item='F'),
    'G': Sku('G', 20),
    'H': Sku('H', 10, offer_unit=5, offer_price=45, extra_offer_unit=10, extra_offer_price=80),
    'I': Sku('I', 35),
    'J': Sku('J', 60),
    'K': Sku('K', 70, offer_unit=2, offer_price=120),
    'L': Sku('L', 90),
    'M': Sku('M', 15),
    'N': Sku('N', 40, free_offer_unit=3, free_offer_item='M'),
    'O': Sku('O', 10),
    'P': Sku('P', 50, offer_unit=5, offer_price=200),
    'Q': Sku('Q', 30, offer_unit=3, offer_price=80),
    'R': Sku('R', 50, free_offer_unit=3, free_offer_item='Q'),
    'S': Sku('S', 20),
    'T': Sku('T', 20),
    'U': Sku('U', 40, free_offer_unit=3, free_offer_item='U'),
    'V': Sku('V', 50, offer_unit=2, offer_price=90, extra_offer_unit=3, extra_offer_price=130),
    'W': Sku('W', 20),
    'X': Sku('X', 17),
    'Y': Sku('Y', 20),
    'Z': Sku('Z', 21),
}


# skus = unicode string
def checkout(skus):
    # for any illegal input return -1
    if not re.search(r'^[A-Z]*$', skus):
        return -1

    # get count of each item
    item_counts = Counter(skus)

    # apply free unit discounts
    [store_skus[item].apply_free_item_offer(item_counts) for item in item_counts]

    total = 0
    # apply group discount
    # sort list by sku price in descending order, chop off most expensive ones in batches of 3
    group_offer_items = 'STXYZ'
    group_offer_list = []
    for sku in skus:
        if sku in group_offer_items:
            item_counts[sku] = 0
            group_offer_list += sku
    group_offer_list = sorted(group_offer_list, key=lambda s: store_skus[s].price, reverse=True)
    group_count = group_offer_list // 5


    YXZZ
    ZZYX
    # calculate total price for basket
    for item in item_counts:
        total += store_skus[item].calculate_price(item_counts[item])
    return total




