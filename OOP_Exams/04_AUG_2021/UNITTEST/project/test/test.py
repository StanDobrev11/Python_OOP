from project.pet_shop import PetShop

import unittest


class TestPetShop(unittest.TestCase):
    def setUp(self) -> None:
        self.test = PetShop('name')

    def test_proper_init(self):
        self.assertEqual('name', self.test.name)
        self.assertEqual({}, self.test.food)
        self.assertEqual([], self.test.pets)

    def test_add_food_raises_value_error(self):
        test_case = [-1, 0]
        for x in test_case:
            with self.assertRaises(ValueError) as ve:
                self.test.add_food('test', x)
            self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food_not_yet_in(self):
        actual = self.test.add_food('test', 10)
        expected = "Successfully added 10.00 grams of test."
        self.assertEqual(expected, actual)
        self.assertEqual({'test': 10}, self.test.food)

    def test_add_food_already_in(self):
        self.test.add_food('test', 10)
        self.assertEqual({'test': 10}, self.test.food)
        actual = self.test.add_food('test', 10)
        expected = "Successfully added 10.00 grams of test."
        self.assertEqual(expected, actual)
        self.assertEqual({'test': 20}, self.test.food)

    def test_add_two_types_food(self):
        self.test.add_food('test', 10)
        self.test.add_food('test2', 70)
        self.assertEqual({'test': 10, 'test2': 70}, self.test.food)

    def test_add_pet_valid(self):
        actual = self.test.add_pet('Puppy')
        expected = "Successfully added Puppy."
        self.assertEqual(expected, actual)
        self.assertEqual(['Puppy'], self.test.pets)

    def test_add_pet_already_in(self):
        self.test.add_pet('Puppy')
        self.test.add_pet('Maggi')
        self.test.add_pet('Catty')
        with self.assertRaises(Exception) as ex:
            self.test.add_pet('Catty')
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_raises_exception(self):
        self.test.add_pet('Puppy')
        self.test.add_pet('Maggi')
        self.test.add_food('test', 10)
        self.test.add_food('test2', 70)
        with self.assertRaises(Exception) as ex:
            self.test.feed_pet('test', 'Catty')
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_missing_food(self):
        self.test.add_pet('Puppy')
        self.test.add_pet('Maggi')
        self.test.add_food('test', 10)
        self.test.add_food('test2', 70)
        actual = self.test.feed_pet('test3', 'Maggi')
        expected = 'You do not have test3'
        self.assertEqual(expected, actual)

    def test_feed_pet_adding_more_food_if_food_less_than_100(self):
        self.test.add_pet('Puppy')
        self.test.add_pet('Maggi')
        self.test.add_food('test', 10)
        self.test.add_food('test2', 70)
        actual = self.test.feed_pet('test', 'Maggi')
        expected = "Adding food..."
        self.assertEqual(expected, actual)
        self.assertEqual({'test': 1010, 'test2': 70}, self.test.food)

    def test_feed_pet_success(self):
        self.test.add_pet('Maggi')
        self.test.add_food('test', 1000)
        expected = "Maggi was successfully fed"
        actual = self.test.feed_pet('test', 'Maggi')
        self.assertEqual(expected, actual)
        self.assertEqual({'test': 900}, self.test.food)

    def test_repr(self):
        self.test.add_pet('Puppy')
        self.test.add_pet('Maggi')
        expected = 'Shop name:\nPets: Puppy, Maggi'
        actual = self.test.__repr__()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()