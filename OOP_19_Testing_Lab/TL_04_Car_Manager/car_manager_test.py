from OOP_19_Testing_Lab.TL_04_Car_Manager.car_manager import Car
import unittest


class TestCar(unittest.TestCase):

    def test_proper_init_method(self):
        c = Car('BMW', 'M316', 10, 60)
        self.assertEqual(c.make, 'BMW')
        self.assertEqual(c.model, 'M316')
        self.assertEqual(c.fuel_consumption, 10)
        self.assertEqual(c.fuel_capacity, 60)
        self.assertEqual(c.fuel_amount, 0)

    def test_make_attr_non_proper_value(self):
        c = Car('BMW', 'M316', 10, 60)
        with self.assertRaises(Exception) as context:
            c.make = ''
        self.assertEqual(type(context.exception), Exception)
        self.assertEqual(str(context.exception), 'Make cannot be null or empty!')
        with self.assertRaises(Exception) as context:
            c.make = None
        self.assertEqual(type(context.exception), Exception)
        self.assertEqual(str(context.exception), 'Make cannot be null or empty!')

    def test_model_attr_non_proper_value(self):
        c = Car('BMW', 'M316', 10, 60)
        with self.assertRaises(Exception) as context:
            c.model = ''
        self.assertEqual(type(context.exception), Exception)
        self.assertEqual(str(context.exception), 'Model cannot be null or empty!')
        with self.assertRaises(Exception) as context:
            c.model = None
        self.assertEqual(type(context.exception), Exception)
        self.assertEqual(str(context.exception), 'Model cannot be null or empty!')

    def test_fuel_consumption_attr_non_proper_value(self):
        c = Car('BMW', 'M316', 10, 60)
        with self.assertRaises(Exception) as context:
            c.fuel_consumption = 0
        self.assertEqual(type(context.exception), Exception)
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")
        with self.assertRaises(Exception) as context:
            c.fuel_consumption = -5
        self.assertEqual(type(context.exception), Exception)
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_attr_non_proper_value(self):
        c = Car('BMW', 'M316', 10, 60)
        with self.assertRaises(Exception) as context:
            c.fuel_capacity = 0
        self.assertEqual(type(context.exception), Exception)
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")
        with self.assertRaises(Exception) as context:
            c.fuel_capacity = -5
        self.assertEqual(type(context.exception), Exception)
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_mount_attr_non_proper_value(self):
        c = Car('BMW', 'M316', 10, 60)
        with self.assertRaises(Exception) as context:
            c.fuel_amount = -5
        self.assertEqual(type(context.exception), Exception)
        self.assertEqual(str(context.exception), "Fuel amount cannot be negative!")

    def test_refuel_negative_fuel_amount(self):
        c = Car('BMW', 'M316', 10, 60)
        with self.assertRaises(Exception) as context:
            c.refuel(-5)
        self.assertEqual(type(context.exception), Exception)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_zero_fuel_amount(self):
        c = Car('BMW', 'M316', 10, 60)
        with self.assertRaises(Exception) as context:
            c.refuel(0)
        self.assertEqual(type(context.exception), Exception)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_proper_refuel_max_capacity(self):
        c = Car('BMW', 'M316', 10, 60)
        c.refuel(5)
        self.assertEqual(c.fuel_amount, 5)
        c.refuel(61)
        self.assertEqual(c.fuel_amount, c.fuel_capacity)

    def test_drive_proper_fuel_rob(self):
        c = Car('BMW', 'M316', 10, 60)
        c.fuel_amount = 10
        c.drive(100)
        self.assertEqual(c.fuel_amount, 0)

    def test_drive_negative_fuel_rob(self):
        c = Car('BMW', 'M316', 10, 60)
        c.fuel_amount = 10
        with self.assertRaises(Exception) as context:
            c.drive(200)
        self.assertEqual(type(context.exception), Exception)
        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")


if __name__ == '__main__':
    unittest.main()
