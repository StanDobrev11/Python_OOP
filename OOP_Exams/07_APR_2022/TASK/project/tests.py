import unittest

from project.controller import Controller
from project.player import Player


class TestController(unittest.TestCase):
    def setUp(self) -> None:
        Player.clear_used_names()
        self.first_player = Player('Peter', 15)
        self.second_player = Player('Lilly', 12, 94)
        self.third_player = Player('Stoyan', 22)
        self.forth_player = Player('Ivan', 23, 99)

    def test_create_same_name_player(self):
        with self.assertRaises(Exception) as ex:
            Player('Peter', 13)
        self.assertEqual("Name Peter is already used!", str(ex.exception))

    def test_add_player_adds_player(self):
        c = Controller()
        actual = c.add_player(self.first_player, self.second_player, self.third_player, self.forth_player)
        expected = "Successfully added: Peter, Lilly, Stoyan, Ivan"
        self.assertEqual(expected, actual)

    def test_add_same_player(self):
        c = Controller()
        actual = c.add_player(self.first_player, self.second_player, self.first_player)
        expected = "Successfully added: Peter, Lilly"
        self.assertEqual(expected, actual)

    def test_add_no_players(self):
        c = Controller()
        actual = c.add_player()
        expected = "Successfully added: "
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
