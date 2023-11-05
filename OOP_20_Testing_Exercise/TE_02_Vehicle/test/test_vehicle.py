import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.test_vehicle = Vehicle(10.5, 125)

    def test_class_attributes(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_proper_instance_initialization(self):
        self.assertEqual(10.5, self.test_vehicle.fuel)
        self.assertEqual(125, self.test_vehicle.horse_power)
        self.assertEqual(10.5, self.test_vehicle.capacity)
        self.assertEqual(1.25, self.test_vehicle.fuel_consumption)

    def test_drive_method_proper_fuel_calculation(self):
        self.test_vehicle.drive(1)
        self.assertEqual(9.25, self.test_vehicle.fuel)

    def test_drive_method_raises_fuel_error(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.drive(100)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_refuel_method_proper_fuel_calculation(self):
        self.test_vehicle.fuel = 5
        self.test_vehicle.refuel(5)
        self.assertEqual(10, self.test_vehicle.fuel)

    def test_refuel_method_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.refuel(5)
        self.assertEqual('Too much fuel', str(ex.exception))

    def test_str_method(self):
        expected = f"The vehicle has 125 horse power with 10.5 fuel left and 1.25 fuel consumption"
        actual = self.test_vehicle.__str__()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
