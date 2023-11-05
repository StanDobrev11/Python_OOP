import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self) -> None:
        self.my_hero = Hero('Baltazar', 1, 50, 100)
        self.enemy = Hero('Enemy', 4, 55, 110)

    def test_proper_init(self):
        self.assertEqual('Baltazar', self.my_hero.username)
        self.assertEqual(1, self.my_hero.level)
        self.assertEqual(50, self.my_hero.health)
        self.assertEqual(100, self.my_hero.damage)

    def test_str_method(self):
        expected = "Hero Baltazar: 1 lvl\nHealth: 50\nDamage: 100\n"
        actual = self.my_hero.__str__()
        self.assertEqual(expected, actual)

    def test_battle_same_enemy_hero_name_raises_exception(self):
        self.enemy.username = 'Baltazar'
        with self.assertRaises(Exception) as ex:
            self.my_hero.battle(self.enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_own_health_equals_zero_raise_value_error(self):
        self.my_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.my_hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_own_health_less_than_zero_raise_value_error(self):
        self.my_hero.health = -10
        with self.assertRaises(ValueError) as ve:
            self.my_hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_enemy_health_equals_zero_raise_value_error(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.my_hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception))

    def test_battle_enemy_health_less_than_zero_raise_value_error(self):
        self.enemy.health = -10
        with self.assertRaises(ValueError) as ve:
            self.my_hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception))

    def test_battle_ended_as_draw(self):
        self.my_hero = Hero('Baltazar', 1, 50, 100)
        self.enemy = Hero('Enemy', 1, 50, 100)
        self.assertEqual('Draw', self.my_hero.battle(self.enemy))

    def test_battle_won(self):
        self.my_hero = Hero('Baltazar', 1, 50, 100)
        self.enemy = Hero('Enemy', 1, 50, 10)
        self.assertEqual('You win', self.my_hero.battle(self.enemy))
        self.assertEqual(2, self.my_hero.level)
        self.assertEqual(45, self.my_hero.health)
        self.assertEqual(105, self.my_hero.damage)

    def test_battle_lost(self):
        self.my_hero = Hero('Baltazar', 1, 50, 10)
        self.enemy = Hero('Enemy', 1, 50, 100)
        self.assertEqual('You lose', self.my_hero.battle(self.enemy))
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(45, self.enemy.health)
        self.assertEqual(105, self.enemy.damage)


if __name__ == '__main__':
    unittest.main()
