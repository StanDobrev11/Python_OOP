import unittest
from collections import deque

from project.railway_station import RailwayStation


class TestRailwayStation(unittest.TestCase):

    def setUp(self) -> None:
        self.rs = RailwayStation('test')

    def test_proper_init_method(self):
        self.assertEqual('test', self.rs.name)
        self.assertEqual(deque([]), self.rs.arrival_trains)
        self.assertEqual(deque([]), self.rs.departure_trains)

    def test_name_not_valid_raises_error(self):
        test_case = ['', 'a', 'bb', 'ccc']
        expected = "Name should be more than 3 symbols!"
        for case in test_case:
            with self.assertRaises(ValueError) as ve:
                self.rs.name = case
            self.assertEqual(expected, str(ve.exception))

    def test_add_new_arrival_on_board_method(self):
        self.rs.new_arrival_on_board('train1')
        self.rs.new_arrival_on_board('train2')
        expected = deque(['train1', 'train2'])
        actual = self.rs.arrival_trains
        self.assertEqual(expected, actual)

    def test_train_has_arrived_actual_train_success(self):
        self.rs.new_arrival_on_board('train1')
        self.rs.new_arrival_on_board('train2')

        expected = "train1 is on the platform and will leave in 5 minutes."
        actual = self.rs.train_has_arrived('train1')

        self.assertEqual(expected, actual)
        self.assertEqual(deque(['train1']), self.rs.departure_trains)

    def test_train_has_arrived_other_trains_before_this_train(self):
        self.rs.new_arrival_on_board('train1')
        self.rs.new_arrival_on_board('train2')

        expected = "There are other trains to arrive before train2."
        actual = self.rs.train_has_arrived('train2')

        self.assertEqual(expected, actual)
        self.assertEqual(deque([]), self.rs.departure_trains)

    def test_train_has_arrived_no_trains_in_queue_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.rs.train_has_arrived('train1')
        self.assertEqual('pop from an empty deque', str(ie.exception))

    def test_train_has_arrived_train_not_in_queue(self):
        self.rs.new_arrival_on_board('train1')
        actual = self.rs.train_has_arrived('train2')
        expected = "There are other trains to arrive before train2."

        self.assertEqual(expected, actual)

    def test_train_has_left_no_departing_trains(self):
        self.assertEqual(deque([]), self.rs.departure_trains)
        self.assertFalse(self.rs.train_has_left('train'))

    def test_train_has_left_not_correct_train(self):
        self.rs.new_arrival_on_board('train1')
        self.rs.train_has_arrived('train1')
        self.assertEqual(deque(['train1']), self.rs.departure_trains)
        self.assertFalse(self.rs.train_has_left('train2'))

    def test_train_has_left_correct(self):
        self.rs.new_arrival_on_board('train1')
        self.rs.new_arrival_on_board('train2')

        self.rs.train_has_arrived('train1')
        self.rs.train_has_arrived('train2')

        self.assertTrue(self.rs.train_has_left('train1'))
        self.assertEqual(deque(['train2']), self.rs.departure_trains)

    def test_train_not_next_in_queue(self):
        self.rs.new_arrival_on_board('train1')
        self.rs.new_arrival_on_board('train2')

        self.rs.train_has_arrived('train1')
        self.rs.train_has_arrived('train2')

        self.assertFalse(self.rs.train_has_left('train2'))


if __name__ == '__main__':
    unittest.main()
