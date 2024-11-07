from decimal import Decimal

class ProductDecorator:
    def __init__(self, product):
        self.product = product

    def add_discount(self, percentage):
        discount_factor = Decimal(percentage) / Decimal(100)
        self.product.price -= self.product.price * discount_factor

    def add_tag(self, tag):
        if not self.product.tags:
            self.product.tags = tag
        else:
            self.product.tags += f", {tag}"
