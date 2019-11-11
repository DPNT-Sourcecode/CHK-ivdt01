import re
from collections import Counter


class Sku:
    def __init__(self, item, price, offer_unit=None, offer_price=None, extra_offer_unit=None, extra_offer_price=None, free_item_for_two=None):
        self.item = item
        self.price = price
        self.offer_unit = offer_unit
        self.offer_price = offer_price
        self.extra_offer_unit = extra_offer_unit
        self.extra_offer_price = extra_offer_price
        self.free_item_for_two = free_item_for_two

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
        if self.free_item_for_two and basket_counts.get(self.free_item_for_two,0) > 0:
            # reduce free item's count by the number of times we could apply the free item offer
            basket_counts[self.free_item_for_two] -= basket_counts[self.item] // 2
            # ensure free item's count is not negative
            basket_counts[self.free_item_for_two] = max(basket_counts[self.free_item_for_two], 0)


store_skus = {
    'A': Sku('A', 50, 3, 130, 5, 200),
    'B': Sku('B', 30, 2, 45),
    'C': Sku('C', 20),
    'D': Sku('D', 15),
    'E': Sku('E', 40, free_item_for_two='B'),
    'F': Sku('E', 40, free_item_for_two='F'),
}


# skus = unicode string
def checkout(skus):
    # for any illegal input return -1
    if not re.search(r'^[A-F]*$', skus):
        return -1

    # get count of each item
    item_counts = Counter(skus)

    # apply free unit discounts
    for item in item_counts:


    # Note: keeping this as simple as this until these requirements get more complicated
    if item_counts.get('E', 0) > 0 and item_counts.get('B', 0) > 0:
        item_counts['B'] -= item_counts['E'] // 2
        item_counts['B'] = max(item_counts['B'], 0)  # ensure B count is not negative

    # calculate total price
    total = 0
    for item in item_counts:
        total += store_skus[item].calculate_price(item_counts[item])
    return total

