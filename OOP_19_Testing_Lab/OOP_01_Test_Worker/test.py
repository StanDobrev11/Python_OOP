from worker import Worker
import unittest


class WorkerTest(unittest.TestCase):

    def test_worker_init(self):
        w = Worker('Ivan', 1500, 200)
        self.assertEqual(w.name, 'Ivan')
        self.assertEqual(w.salary, 1500)
        self.assertEqual(w.energy, 200)

    def test_rest_method(self):
        w = Worker('Ivan', 1500, 200)
        w.rest()
        self.assertEqual(w.energy, 201)

    def test_energy_equal_to_zero_error(self):
        w = Worker('Ivan', 1500, 0)
        with self.assertRaises(Exception) as context:
            w.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_energy_less_than_zero_error(self):
        w = Worker('Ivan', 1500, -10)
        with self.assertRaises(Exception) as context:
            w.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_salary_increase(self):
        w = Worker('Ivan', 1500, 200)
        w.money = 0
        w.money += w.salary
        self.assertEqual(w.money, 1500)

    def test_energy_decrease(self):
        w = Worker('Ivan', 1500, 200)
        w.work()
        self.assertEqual(w.energy, 199)

    def test_get_info_str_value(self):
        w = Worker('Ivan', 1500, 200)
        result = w.get_info()
        self.assertEqual(result, "Ivan has saved 0 money.")


if __name__ == '__main__':
    unittest.main()
