import unittest

from project.controller import Controller
from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food


class TestController(unittest.TestCase):
    def setUp(self) -> None:
        Player.clear_used_names()
        self.first_player = Player('Peter', 15)
        self.second_player = Player('Lilly', 12, 94)
        self.third_player = Player('Stoyan', 22)
        self.forth_player = Player('Ivan', 23, 99)
        self.apple = Food("apple", 22)
        self.cheese = Food("cheese")
        self.juice = Drink("orange juice")
        self.water = Drink("water")
        self.c = Controller()

    def test_create_same_name_player(self):
        with self.assertRaises(Exception) as ex:
            Player('Peter', 13)
        self.assertEqual("Name Peter is already used!", str(ex.exception))

    def test_add_player_adds_player(self):
        actual = self.c.add_player(self.first_player, self.second_player, self.third_player, self.forth_player)
        expected = "Successfully added: Peter, Lilly, Stoyan, Ivan"
        self.assertEqual(expected, actual)

    def test_add_same_player(self):
        actual = self.c.add_player(self.first_player, self.second_player, self.first_player)
        expected = "Successfully added: Peter, Lilly"
        self.assertEqual(expected, actual)

    def test_add_no_players(self):
        actual = self.c.add_player()
        expected = "Successfully added: "
        self.assertEqual(expected, actual)

    def test_sustain_supply_type_not_valid(self):
        self.c.add_player(self.first_player)
        self.assertIsNone(self.c.sustain('Peter', 'NotValid'))

    def test_sustain_player_not_in_list(self):
        self.c.add_player(self.first_player)
        self.assertIsNone(self.c.sustain('NotInList', 'Food'))

    def test_sustain_player_enough_stamina(self):
        self.c.add_player(self.first_player)
        self.assertTrue(100, self.first_player.stamina)
        self.assertFalse(self.first_player.need_sustenance)

        actual = self.c.sustain('Peter', 'Food')
        expected = "Peter have enough stamina."

        self.assertEqual(expected, actual)

    def test_sustain_no_suitable_supply_raises_exception(self):
        self.c.add_player(self.second_player)
        self.c.add_supply(self.apple, self.cheese)
        self.assertTrue(self.second_player.need_sustenance)

        with self.assertRaises(Exception) as ex:
            self.c.sustain('Lilly', 'Drink')
        self.assertEqual("There are no drink supplies left!", str(ex.exception))


if __name__ == '__main__':
    unittest.main()
