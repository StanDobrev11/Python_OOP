import unittest

from project.movie_app import MovieApp
from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.thriller import Thriller
from project.user import User


class TestUser(unittest.TestCase):

    def setUp(self) -> None:
        self.u = User('test', 22)
        self.movie = Action('Die Hard', 1988, self.u, 18)
        self.movie2 = Action('Free Guy', 2021, self.u, 16)

    def test_name_validator(self):
        with self.assertRaises(ValueError) as ve:
            self.u.username = ''
        self.assertEqual("Invalid username!", str(ve.exception))

    def test_age_validator(self):
        with self.assertRaises(ValueError) as ve:
            self.u.age = 5
        self.assertEqual("Users under the age of 6 are not allowed!", str(ve.exception))

    def test_proper_str(self):
        self.u.movies_owned.append(self.movie)
        self.u.movies_owned.append(self.movie2)
        expected = "Username: test, Age: 22\nLiked movies:\nNo movies liked.\nOwned movies:\nAction - Title:Die Hard, Year:1988, Age restriction:18, Likes:0, Owned by:test\nAction - Title:Free Guy, Year:2021, Age restriction:16, Likes:0, Owned by:test"
        actual = self.u.__str__()
        self.assertEqual(expected, actual)
        expected = f"Username: test, Age: 22\nLiked movies:\nNo movies liked.\nOwned movies:\n{self.movie.details()}\n{self.movie2.details()}"
        actual = self.u.__str__()
        self.assertEqual(expected, actual)


class TestMovie(unittest.TestCase):

    def setUp(self) -> None:
        self.u = User('test', 22)
        self.movie = Thriller('Die Hard', 1988, self.u, 18)
        self.movie2 = Action('Free Guy', 2021, self.u, 16)
        self.movie3 = Fantasy('The Lord of the Rings', 2003, self.u, 14)

    def test_type_proper(self):
        self.assertEqual('Action', self.movie2.type)

    def test_age_restriction(self):
        self.assertEqual(14, self.movie3.age_restriction)

    def test_age_restriction_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.age_restriction = 15
        self.assertEqual("Thriller movies must be restricted for audience under 16 years!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.movie2.age_restriction = 11
        self.assertEqual("Action movies must be restricted for audience under 12 years!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.movie3.age_restriction = 5
        self.assertEqual("Fantasy movies must be restricted for audience under 6 years!", str(ve.exception))

    def test_owner(self):
        self.assertEqual(self.u, self.movie.owner)
        self.assertIsInstance(self.movie.owner, User)


class TestMovieApp(unittest.TestCase):

    def setUp(self) -> None:
        self.m = MovieApp()
        self.u = User('test', 22)
        self.u1 = User('test2', 14)
        self.movie = Thriller('Die Hard', 1988, self.u, 18)
        self.movie2 = Action('Free Guy', 2021, self.u, 16)
        self.movie3 = Fantasy('The Lord of the Rings', 2003, self.u, 14)
        self.movie4 = Action('Dynasty', 1988, self.u)

    def test_register_user(self):
        actual = self.m.register_user('Test', 22)
        expected = "Test registered successfully."
        self.assertEqual(expected, actual)
        self.assertEqual(1, len(self.m.users_collection))

    def test_fail_register_user(self):
        self.m.register_user('Test', 12)
        self.assertEqual(1, len(self.m.users_collection))
        with self.assertRaises(Exception) as ex:
            self.m.register_user('Test', 22)
        expected = "User already exists!"
        self.assertEqual(expected, str(ex.exception))

    def test_upload_movie_not_registered_user(self):
        with self.assertRaises(Exception) as ex:
            self.m.upload_movie('Test', self.movie)
        self.assertEqual("This user does not exist!", str(ex.exception))

    def test_upload_owner_different(self):
        self.m.register_user('Test', 55)
        with self.assertRaises(Exception) as ex:
            self.m.upload_movie('Test', self.movie)
        self.assertEqual("Test is not the owner of the movie Die Hard!", str(ex.exception))

    def test_upload_movie_already_added(self):
        self.m.register_user('Test', 22)
        user = self.m.get_existing_user('Test')
        self.movie.owner = user
        self.m.upload_movie('Test', self.movie)
        with self.assertRaises(Exception) as ex:
            self.m.upload_movie('Test', self.movie)
        self.assertEqual("Movie already added to the collection!", str(ex.exception))
        self.assertEqual(self.m.movies_collection[0], self.movie)
        self.assertEqual(self.m.users_collection[0].movies_owned[0], self.movie)

    def test_upload_success(self):
        self.m.register_user('Test', 22)
        user = self.m.get_existing_user('Test')
        self.movie.owner = user
        actual = self.m.upload_movie('Test', self.movie)
        expected = "Test successfully added Die Hard movie."
        self.assertEqual(expected, actual)
        self.assertEqual(self.m.movies_collection[0], self.movie)
        self.assertEqual(self.m.users_collection[0].movies_owned[0], self.movie)

    def test_edit_movie_movie_not_found(self):
        self.m.register_user('Test', 22)

        with self.assertRaises(Exception) as ex:
            self.m.edit_movie('Test', self.movie)
        self.assertEqual("The movie Die Hard is not uploaded!", str(ex.exception))

    def test_edit_movie_not_owner(self):
        self.m.register_user('Test', 22)
        with self.assertRaises(Exception) as ex:
            self.m.upload_movie('Test', self.movie)
        self.assertEqual("Test is not the owner of the movie Die Hard!", str(ex.exception))

    def test_set_movie_attributes(self):
        self.m.register_user('Test', 22)
        self.movie.owner = self.m.users_collection[0]
        self.m.upload_movie('Test', self.movie)

        actual = self.m.edit_movie('Test', self.movie, year=2000, age_restriction=20, title='ChangedTitle')

        self.assertEqual(2000, self.movie.year)
        self.assertEqual(20, self.movie.age_restriction)
        self.assertEqual('ChangedTitle', self.movie.title)

        expected = "Test successfully edited ChangedTitle movie."
        self.assertEqual(expected, actual)

    def test_like_movie_owned_movie(self):
        self.m.register_user('Test', 22)
        self.movie.owner = self.m.users_collection[0]
        self.m.upload_movie('Test', self.movie)

        with self.assertRaises(Exception) as ex:
            self.m.like_movie('Test', self.movie)
        self.assertEqual("Test is the owner of the movie Die Hard!", str(ex.exception))
        self.assertEqual(0, self.movie.likes)

    def test_like_movie(self):
        self.m.register_user('Test', 22)
        self.m.register_user('Test2', 21)
        user = self.m.get_existing_user('Test')
        user2 = self.m.get_existing_user('Test2')
        self.movie.owner = user
        self.m.upload_movie('Test', self.movie)
        actual = self.m.like_movie('Test2', self.movie)
        expected = "Test2 liked Die Hard movie."
        self.assertEqual(expected, actual)
        self.assertEqual(1, self.movie.likes)
        self.assertEqual(self.movie, user2.movies_liked[0])

    def test_display_movies_no_movies(self):
        expected = "No movies found."
        actual = self.m.display_movies()
        self.assertEqual(expected, actual)

    def test_display_movies(self):
        self.m.register_user('test', 20)
        self.m.register_user('test2', 18)
        user = self.m.get_existing_user('test')
        user2 = self.m.get_existing_user('test2')
        self.movie4.owner = user2
        self.movie.owner = user2
        self.movie2.owner = user
        self.movie3.owner = user
        self.m.upload_movie('test2', self.movie)
        self.m.upload_movie('test2', self.movie4)
        self.m.upload_movie('test', self.movie2)
        self.m.upload_movie('test', self.movie3)

        expected = f"{self.movie2.details()}\n{self.movie3.details()}\n{self.movie.details()}\n{self.movie4.details()}"
        actual = self.m.display_movies()
        self.assertEqual(expected, actual)

    def test_str_method_no_user_no_movies(self):
        expected = "All users: No users.\nAll movies: No movies."
        actual = str(self.m)
        self.assertEqual(expected, actual)

    def test_str_method_movies_user(self):
        self.m.register_user('test', 20)
        self.m.register_user('test2', 18)
        user = self.m.get_existing_user('test')
        user2 = self.m.get_existing_user('test2')
        self.movie4.owner = user2
        self.movie.owner = user2
        self.movie2.owner = user
        self.movie3.owner = user
        self.m.upload_movie('test2', self.movie)
        self.m.upload_movie('test2', self.movie4)
        self.m.upload_movie('test', self.movie2)
        self.m.upload_movie('test', self.movie3)

        expected = "All users: test, test2\nAll movies: Die Hard, Dynasty, Free Guy, The Lord of the Rings"
        actual = str(self.m)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
