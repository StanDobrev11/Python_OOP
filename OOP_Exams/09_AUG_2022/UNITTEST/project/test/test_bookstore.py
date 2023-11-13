from project.bookstore import Bookstore

import unittest


class TestBookstore(unittest.TestCase):
    def setUp(self) -> None:
        self.b = Bookstore(1)

    def test_init(self):
        self.assertEqual(1, self.b.books_limit)
        self.assertEqual({}, self.b.availability_in_store_by_book_titles)
        self.assertEqual(0, self.b.total_sold_books)
        self.assertEqual(0, self.b._Bookstore.__total_sold_books)

    def test_total_sold_not_possible_to_set(self):
        with self.assertRaises(AttributeError):
            self.b.total_sold_books = 5

    def test_books_limit_setter(self):
        tests = [0, -1]
        with self.assertRaises(ValueError) as ve:
            for x in tests:
                self.b.books_limit = x
            self.assertEqual(f"Books limit of {x} is not valid", str(ve.exception))

    def test_len(self):
        self.assertEqual(0, len(self.b))

    def test_receive_book_adds_book_success(self):
        actual = self.b.receive_book('Title', 1)
        expected = "1 copies of Title are available in the bookstore."
        self.assertEqual(1, len(self.b))
        self.assertEqual(expected, actual)

    def test_add_book_second_copy(self):
        self.b.books_limit = 2
        self.b.receive_book('Title', 1)
        actual = self.b.receive_book('Title', 1)
        expected = "2 copies of Title are available in the bookstore."
        self.assertEqual(2, len(self.b))
        self.assertEqual(expected, actual)

    def test_add_book_limit_reach(self):
        self.b.books_limit = 2
        self.b.receive_book('Title', 2)
        with self.assertRaises(Exception) as ex:
            self.b.receive_book('Tilte', 1)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_sell_success(self):
        self.b.receive_book('Title', 1)
        actual = self.b.sell_book('Title', 1)
        expected = "Sold 1 copies of Title"
        self.assertEqual(expected, actual)

    def test_sell_increasing_total_sold(self):
        self.b.receive_book('Title', 1)
        self.b.sell_book('Title', 1)
        self.assertEqual(1, self.b.total_sold_books)

    def test_sell_raises_ex_not_enough_copies(self):
        self.b.receive_book('Title', 1)
        with self.assertRaises(Exception) as ex:
            self.b.sell_book('Title', 2)
        self.assertEqual("Title has not enough copies to sell. Left: 1", str(ex.exception))

    def test_sell_exception_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.b.sell_book('Title', 1)
        self.assertEqual("Book Title doesn't exist!", str(ex.exception))

    def test_str(self):
        self.b.books_limit = 10
        self.b.receive_book('Title', 4)
        self.b.receive_book('New Book', 2)
        self.b.receive_book('Test', 2)

        self.assertEqual(8, len(self.b))
        self.assertEqual(0, self.b.total_sold_books)

        self.b.sell_book('Title', 3)
        self.b.sell_book('Test', 1)
        self.b.sell_book('New Book', 2)

        self.assertEqual(2, len(self.b))
        self.assertEqual(6, self.b.total_sold_books)

        expected = "Total sold books: 6\nCurrent availability: 2\n - Title: 1 copies\n - New Book: 0 copies\n - Test: 1 copies"
        actual = str(self.b)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
