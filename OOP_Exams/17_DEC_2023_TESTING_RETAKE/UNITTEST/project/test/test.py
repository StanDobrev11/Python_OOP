import unittest

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(unittest.TestCase):

    def setUp(self) -> None:
        self.r = ClimbingRobot('Mountain', 'Part', 10, 10)

    def test_proper_init(self):
        self.assertEqual('Mountain', self.r.category)
        self.assertEqual('Part', self.r.part_type)
        self.assertEqual(10, self.r.capacity)
        self.assertEqual(10, self.r.memory)
        self.assertEqual([], self.r.installed_software)

    def test_class_var(self):
        self.assertEqual(['Mountain', 'Alpine', 'Indoor', 'Bouldering'], self.r.ALLOWED_CATEGORIES)

    def test_category_proper_setter(self):
        for case in ['Mountain', 'Alpine', 'Indoor', 'Bouldering']:
            self.r.category = case
            self.assertEqual(case, self.r.category)

    def test_category_prop_raises_error(self):
        test_case = ['Test', ' ', 5, -1, 3.14, 'NOT VALID']
        for case in test_case:
            with self.assertRaises(ValueError) as ve:
                self.r.category = case
            self.assertEqual(f"Category should be one of {self.r.ALLOWED_CATEGORIES}", str(ve.exception))

    def test_install_software_success(self):
        software = {
            'name': 'test software',
            'capacity_consumption': 10,
            'memory_consumption': 10,
        }
        actual = self.r.install_software(software)
        expected = "Software 'test software' successfully installed on Mountain part."
        self.assertEqual(expected, actual)

    def test_install_software_capacity_error(self):
        software = {
            'name': 'test software',
            'capacity_consumption': 11,
            'memory_consumption': 10,
        }
        expected = "Software 'test software' cannot be installed on Mountain part."
        actual = self.r.install_software(software)
        self.assertEqual(expected, actual)

    def test_install_software_memory_error(self):
        software = {
            'name': 'test software',
            'capacity_consumption': 10,
            'memory_consumption': 11,
        }
        expected = "Software 'test software' cannot be installed on Mountain part."
        actual = self.r.install_software(software)
        self.assertEqual(expected, actual)

    # def test_get_used_capacity(self):
    #     software = {
    #         'name': 'test software',
    #         'capacity_consumption': 3,
    #         'memory_consumption': 4,
    #     }
    #     software_1 = {
    #         'name': 'test software',
    #         'capacity_consumption': 2,
    #         'memory_consumption': 2,
    #     }
    #
    #     self.r.install_software(software)
    #     self.r.install_software(software_1)
    #
    #     self.assertEqual(5, self.r.get_used_capacity())

    def test_get_available_capacity(self):

        software = {
            'name': 'test software',
            'capacity_consumption': 3,
            'memory_consumption': 4,
        }
        software_1 = {
            'name': 'test software',
            'capacity_consumption': 2,
            'memory_consumption': 2,
        }

        self.r.install_software(software)
        self.r.install_software(software_1)

        self.assertEqual(5, self.r.get_available_capacity())

    def test_get_available_memory(self):

        software = {
            'name': 'test software',
            'capacity_consumption': 3,
            'memory_consumption': 4,
        }
        software_1 = {
            'name': 'test software',
            'capacity_consumption': 2,
            'memory_consumption': 2,
        }

        self.r.install_software(software)
        self.r.install_software(software_1)

        self.assertEqual(4, self.r.get_available_memory())

    # def test_get_used_memory(self):
    #
    #     software = {
    #         'name': 'test software',
    #         'capacity_consumption': 3,
    #         'memory_consumption': 4,
    #     }
    #     software_1 = {
    #         'name': 'test software',
    #         'capacity_consumption': 2,
    #         'memory_consumption': 2,
    #     }
    #
    #     self.r.install_software(software)
    #     self.r.install_software(software_1)
    #
    #     self.assertEqual(6, self.r.get_used_memory())


if __name__ == '__main__':
    unittest.main()
