from project.shopping_cart import ShoppingCart

import unittest


class TestShoppingCart(unittest.TestCase):
    def setUp(self) -> None:
        self.s = ShoppingCart('Test', 10)

    def test_init(self):
        self.assertEqual('Test', self.s.shop_name)
        self.assertEqual(10, self.s.budget)
        self.assertEqual({}, self.s.products)

    def test_validator_capital_letter(self):
        with self.assertRaises(ValueError) as ve:
            self.s.shop_name = 'test'
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_validator_raises_exception(self):
        test_case = [chr(i) for i in range(65)]
        test_case.extend([chr(i) for i in range(123, 128)])
        for x in test_case:
            with self.assertRaises(ValueError) as ve:
                test = ShoppingCart(x, 10)
            self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_validator_valid_name(self):
        valid_alpha_symbols = [chr(i) for i in range(65, 91)]  # Uppercase letters (A-Z)
        valid_alpha_symbols.extend([chr(i) for i in range(97, 123)])  # Lowercase letters (a-z)
        for x in valid_alpha_symbols:
            other = ShoppingCart(x.upper(), 10)
            self.assertEqual(x.upper(), other.shop_name)

    def test_add_to_cart_success(self):
        actual = self.s.add_to_cart('TT', 8)
        expected = "TT product was successfully added to the cart!"
        self.assertEqual(expected, actual)
        self.assertEqual({'TT': 8}, self.s.products)

    def test_add_to_cart_raises_exception(self):
        test_case = [100, 101]
        for x in test_case:
            with self.assertRaises(ValueError) as ve:
                self.s.add_to_cart('TT', x)
            self.assertEqual("Product TT cost too much!", str(ve.exception))

    def test_remove_from_cart_success(self):
        self.s.add_to_cart('TT', 8)
        self.assertEqual({'TT': 8}, self.s.products)

        actual = self.s.remove_from_cart('TT')
        expected = "Product TT was successfully removed from the cart!"
        self.assertEqual(expected, actual)
        self.assertEqual({}, self.s.products)

    def test_remove_from_cart_no_item_error(self):
        with self.assertRaises(ValueError) as ve:
            self.s.remove_from_cart('TT')
        self.assertEqual("No product with name TT in the cart!", str(ve.exception))

    def test_buy_success(self):
        prices = [8, 10]
        for x in prices:
            self.s.add_to_cart('TT', x)
            actual = self.s.buy_products()
            expected = f'Products were successfully bought! Total cost: {x:.2f}lv.'
            self.assertEqual(expected, actual)

    def test_buy_error(self):
        self.s.add_to_cart('TT', 11)
        with self.assertRaises(ValueError) as ve:
            self.s.buy_products()
        expected = "Not enough money to buy the products! Over budget with 1.00lv!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_method(self):
        other = ShoppingCart('Other', 12)
        self.s.add_to_cart('TT', 3)
        self.s.add_to_cart('T1', 6)
        other.add_to_cart('Mm', 7)

        result = self.s + other
        self.assertIsInstance(result, ShoppingCart)
        self.assertEqual('TestOther', result.shop_name)
        self.assertEqual(22, result.budget)
        self.assertEqual({'TT': 3, 'T1': 6, 'Mm': 7}, result.products)


if __name__ == '__main__':
    unittest.main()
