import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self) -> None:
        self.m = Mammal('Wolf', 'K9', 'woff')

    def test_proper_init(self):
        self.assertEqual('Wolf', self.m.name)
        self.assertEqual('K9', self.m.type)
        self.assertEqual('woff', self.m.sound)
        self.assertEqual("animals", self.m._Mammal__kingdom)

    def test_make_sound(self):
        result = self.m.make_sound()
        expected_result = 'Wolf makes woff'
        self.assertEqual(expected_result, result)

    def test_get_kingdom(self):
        self.assertEqual(self.m._Mammal__kingdom, self.m.get_kingdom())

    def test_info(self):
        result = self.m.info()
        expected_result = f"{self.m.name} is of type {self.m.type}"
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
