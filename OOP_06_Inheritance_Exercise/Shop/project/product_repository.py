from project.product import Product
from typing import ClassVar


class ProductRepository:
    """
    It is a repository for all products that are delivered to the grocery shop.
    """

    def __init__(self):
        self.products: list[ClassVar] = []

    def __repr__(self):
        # "{product_name1}: {quantity1}\n{product_name2}: {quantity2}\n..."
        return '\n'.join(f"{product.name}: {product.quantity}" for product in self.products)

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str):
        try:
            product = next(filter(lambda n: n.name == product_name, self.products))
            return product
        except StopIteration:
            pass

    def remove(self, product_name: str):
        try:
            product = next(filter(lambda n: n.name == product_name, self.products))
            self.products.remove(product)
        except StopIteration:
            pass
