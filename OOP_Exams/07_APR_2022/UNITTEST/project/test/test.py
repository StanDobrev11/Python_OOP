import unittest

from project.movie import Movie


class TestMovie(unittest.TestCase):
    def setUp(self) -> None:
        self.m = Movie('Prey', 2022, 7.5)

    def test_proper_init(self):
        self.assertEqual('Prey', self.m.name)
        self.assertEqual(2022, self.m.year)
        self.assertEqual(7.5, self.m.rating)

    def test_name_validator_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.m.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_validator_raises_error(self):
        tests = [1885, 1886]
        for case in tests:
            with self.assertRaises(ValueError) as ve:
                self.m.year = case
            self.assertEqual("Year is not valid!", str(ve.exception))

    def test_year_validator_passes(self):
        self.m.year = 1887
        self.assertEqual(1887, self.m.year)

    def test_add_actor_success(self):
        self.assertIsNone(self.m.add_actor('Ivan'))
        self.assertEqual(['Ivan'], self.m.actors)

    def test_add_actors_already_added(self):
        self.m.add_actor('Ivan')
        expected = "Ivan is already added in the list of actors!"
        actual = self.m.add_actor('Ivan')
        self.assertEqual(expected, actual)
        self.assertEqual(['Ivan'], self.m.actors)

    def test_gt_method_positive_outcome(self):
        this_movie = self.m
        other_movie = Movie('Lucy', 2021, 7)
        expected = '"Prey" is better than "Lucy"'
        actual = this_movie > other_movie
        self.assertEqual(expected, actual)

    def test_gt_method_negative_outcome(self):
        this_movie = self.m
        other_movie = Movie('Lucy', 2021, 8)
        expected = '"Lucy" is better than "Prey"'
        actual = this_movie > other_movie
        self.assertEqual(expected, actual)

    def test_repr_method(self):
        self.m.add_actor('Ivan')
        self.m.add_actor('Stoyan')
        self.m.add_actor('Dragan')
        expected = f"Name: Prey\nYear of Release: 2022\nRating: 7.50\nCast: Ivan, Stoyan, Dragan"
        actual = self.m.__repr__()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
