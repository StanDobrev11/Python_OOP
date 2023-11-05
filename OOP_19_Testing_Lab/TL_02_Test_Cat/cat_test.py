from cat import Cat

import unittest


class TestCat(unittest.TestCase):

    def test_cat_size_eat_method(self):
        c = Cat('Kitty')
        c.fed = False
        c.size = 0
        c.eat()
        self.assertEqual(c.size, 1)

    def test_cat_fed_eat_method(self):
        c = Cat('Kitty')
        c.fed = False
        c.eat()
        self.assertTrue(c.fed)

    def test_cat_is_full_eat_method(self):
        c = Cat('Kitty')
        c.fed = True
        with self.assertRaises(Exception) as context:
            c.eat()
        self.assertEqual(str(context.exception), 'Already fed.')
        self.assertEqual(type(context.exception), Exception)

    def test_cant_sleep_method(self):
        c = Cat('Kitty')
        c.fed = False
        with self.assertRaises(Exception) as context:
            c.sleep()
        self.assertEqual(str(context.exception), 'Cannot sleep while hungry')
        self.assertEqual(type(context.exception), Exception)

    def test_sleepy_after_sleeping_method(self):
        c = Cat('Kitty')
        c.fed = True
        c.sleepy = True
        c.sleep()
        self.assertFalse(c.sleepy)


if __name__ == '__main__':
    unittest.main()
