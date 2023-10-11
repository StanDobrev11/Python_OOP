class Product:
    def __init__(self, name: str, quantity: int) -> None:
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name}"

    def decrease(self, quantity: int) -> None:
        """
        decreases the quantity of the product only if there is enough

        """
        if self.quantity >= quantity:
            self.quantity -= quantity

    def increase(self, quantity: int) -> None:
        self.quantity += quantity
