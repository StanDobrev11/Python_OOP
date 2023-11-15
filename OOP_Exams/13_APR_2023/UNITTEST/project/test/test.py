from project.tennis_player import TennisPlayer

import unittest


class TestTennisPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.t = TennisPlayer('Test', 20, 0)

    def test_proper_init(self):
        self.assertEqual('Test', self.t.name)
        self.assertEqual(20, self.t.age)
        self.assertEqual(0, self.t.points)
        self.assertEqual([], self.t.wins)

    def test_name_raises_error(self):
        test_case = ['', '1', '12']
        for x in test_case:
            with self.assertRaises(ValueError) as ve:
                self.t.name = x
            self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_error(self):
        with self.assertRaises(ValueError) as ve:
            self.t.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_win_success_tournament_already_won(self):
        self.t.add_new_win('Tour')
        expected = "Tour has been already added to the list of wins!"
        actual = self.t.add_new_win('Tour')
        self.assertEqual(expected, actual)

    def test_add_win_first_win(self):
        self.assertEqual([], self.t.wins)
        self.t.add_new_win('Tour')
        self.assertEqual(['Tour'], self.t.wins)

    def test_lt_method(self):
        self.t.points = 20
        other = TennisPlayer('Other', 20, 30)
        expected = 'Other is a top seeded player and he/she is better than Test'
        self.assertEqual(expected, self.t < other)

    def test_lt_method_2(self):
        self.t.points = 33
        other = TennisPlayer('Other', 20, 30)
        expected = 'Test is a better player than Other'
        self.assertEqual(expected, self.t < other)

    def test_str(self):
        self.t.add_new_win('Tour')
        self.t.add_new_win('Win')

        expected = "Tennis Player: Test\n" \
               "Age: 20\n" \
               "Points: 0.0\n" \
               "Tournaments won: Tour, Win"

        self.assertEqual(expected, str(self.t))

if __name__ == '__main__':
    unittest.main()
