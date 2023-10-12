from typing import Optional

from project.product import Product


class ProductRepository:
    """
    It is a repository for all products that are delivered to the grocery shop.
    """

    def __init__(self) -> None:
        self.products: list[Product] = []

    def __repr__(self) -> str:
        # "{product_name1}: {quantity1}\n{product_name2}: {quantity2}\n..."
        return '\n'.join(f"{product.name}: {product.quantity}" for product in self.products)

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Optional[Product]:
        # use Optional when the other value is "None", when is not, use '|' or 'or' operators.
        try:
            product = next(filter(lambda n: n.name == product_name, self.products))
            return product
        except StopIteration:
            pass

    def remove(self, product_name: str) -> None:
        try:
            product = self.find(product_name)
            self.products.remove(product)
        except ValueError:
            pass
