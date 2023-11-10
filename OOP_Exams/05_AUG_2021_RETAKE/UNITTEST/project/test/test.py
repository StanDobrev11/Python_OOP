import unittest

from project.library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        self.test = Library('lib')

    def test_init(self):
        self.assertEqual('lib', self.test.name)
        self.assertEqual({}, self.test.books_by_authors)
        self.assertEqual({}, self.test.readers)

    def test_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test.name = ''
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_new_author_new_book(self):
        self.test.add_book('King', 'It')
        self.assertEqual({'King': ['It']}, self.test.books_by_authors)

    def test_add_new_book_same_author(self):
        self.test.add_book('King', 'It')
        self.test.add_book('King', 'It Part 2')
        self.assertEqual({'King': ['It', 'It Part 2']}, self.test.books_by_authors)

    def test_add_reader_new_reader(self):
        self.test.add_reader('Ivan')
        self.assertEqual({'Ivan': []}, self.test.readers)

    def test_add_same_reader(self):
        self.test.add_reader('Ivan')
        actual = self.test.add_reader('Ivan')
        expected = "Ivan is already registered in the lib library."
        self.assertEqual(expected, actual)

    def test_add_second_reader(self):
        self.test.add_reader('Ivan')
        self.assertEqual({'Ivan': []}, self.test.readers)
        self.test.add_reader('Dragan')
        self.assertEqual({'Ivan': [], 'Dragan': []}, self.test.readers)

    def test_rent_book_reader_not_registered(self):
        actual = self.test.rent_book('Ivan', 'King', 'It')
        expected = "Ivan is not registered in the lib Library."
        self.assertEqual(expected, actual)

    def test_rent_book_book_author_not_in_library(self):
        self.test.add_reader('Ivan')
        actual = self.test.rent_book('Ivan', 'King', 'It')
        expected = "lib Library does not have any King's books."
        self.assertEqual(expected, actual)

    def test_rent_book_book_not_in_library(self):
        self.test.add_reader('Ivan')
        self.test.add_book('King', 'It')
        actual = self.test.rent_book('Ivan', 'King', 'It Part 2')
        expected = """lib Library does not have King's "It Part 2"."""
        self.assertEqual(expected, actual)

    def test_rent_book_success(self):
        self.test.add_reader('Ivan')
        self.test.add_book('King', 'It')
        self.test.add_book('King', 'It Part 2')
        self.test.add_book('King', 'It Part 3')
        self.assertEqual({'King': ['It', 'It Part 2', 'It Part 3']}, self.test.books_by_authors)

        self.test.rent_book('Ivan', 'King', 'It Part 2')

        self.assertEqual({'Ivan': [{'King': 'It Part 2'}]}, self.test.readers)
        self.assertEqual({'King': ['It', 'It Part 3']}, self.test.books_by_authors)
