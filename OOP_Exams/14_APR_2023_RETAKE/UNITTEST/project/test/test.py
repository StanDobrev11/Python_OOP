from project.robot import Robot

import unittest


class TestRobot(unittest.TestCase):
    def setUp(self) -> None:
        self.r = Robot('101', 'Military', 10, 100)

    def test_init(self):
        self.assertEqual('101', self.r.robot_id)
        self.assertEqual('Military', self.r.category)
        self.assertEqual(10, self.r.available_capacity)
        self.assertEqual(100, self.r.price)
        self.assertEqual([], self.r.hardware_upgrades)
        self.assertEqual([], self.r.software_updates)
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], self.r.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, self.r.PRICE_INCREMENT)

    def test_category_passes(self):
        test_case = ['Military', 'Education', 'Entertainment', 'Humanoids']
        for x in test_case:
            expected = x
            self.r.category = x
            actual = self.r.category
            self.assertEqual(expected, actual)

    def test_category_raises_error(self):
        expected = "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'"
        with self.assertRaises(ValueError) as ve:
            self.r.category = '5'
        self.assertEqual(expected, str(ve.exception))

    def test_price_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.r.price = -1
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_success(self):
        expected = 'Robot 101 was upgraded with HARDWARE.'
        actual = self.r.upgrade('HARDWARE', 10)
        self.assertEqual(expected, actual)
        self.assertEqual(['HARDWARE'], self.r.hardware_upgrades)
        self.assertEqual(115.0, self.r.price)

    def test_upgrade_already_upgraded(self):
        self.r.upgrade('HARDWARE', 10)
        expected = "Robot 101 was not upgraded."
        actual = self.r.upgrade('HARDWARE', 10)
        self.assertEqual(['HARDWARE'], self.r.hardware_upgrades)
        self.assertEqual(115.0, self.r.price)
        self.assertEqual(expected, actual)

    def test_update_success(self):
        expected = 'Robot 101 was updated to version 1.0.'
        actual = self.r.update(1.0, 5)
        self.assertEqual(expected, actual)
        self.assertEqual(5, self.r.available_capacity)
        self.assertEqual([1.0], self.r.software_updates)

    def test_update_not_capacity(self):
        expected = "Robot 101 was not updated."
        actual = self.r.update(1.0, 15)
        self.assertTrue(self.r.available_capacity < 15)
        self.assertEqual(expected, actual)

    def test_not_updated_same_version(self):
        self.r.update(1.0, 5)
        actual = self.r.update(1.0, 5)
        expected = "Robot 101 was not updated."
        self.assertEqual(expected, actual)

    def test_not_updated_older_version(self):
        self.r.update(1.0, 5)
        actual = self.r.update(0.9, 5)
        expected = "Robot 101 was not updated."
        self.assertEqual(expected, actual)

    def test_updated_newer_version(self):
        self.r.update(0.9, 5)
        actual = self.r.update(1.0, 5)
        expected = 'Robot 101 was updated to version 1.0.'
        self.assertEqual(expected, actual)

    def test_gt_expensive(self):
        other = Robot('T-1000', 'Military', 10, 90)
        self.assertTrue(self.r > other)
        expected = 'Robot with ID 101 is more expensive than Robot with ID T-1000.'
        self.assertEqual(expected, self.r > other)

    def test_gt_equal_price(self):
        other = Robot('T-1000', 'Military', 10, 100)
        expected = 'Robot with ID 101 costs equal to Robot with ID T-1000.'
        self.assertEqual(expected, self.r > other)

    def test_gt_less_price(self):
        other = Robot('T-1000', 'Military', 10, 1000)
        expected = 'Robot with ID 101 is cheaper than Robot with ID T-1000.'
        self.assertEqual(expected, self.r > other)


if __name__ == '__main__':
    unittest.main()
