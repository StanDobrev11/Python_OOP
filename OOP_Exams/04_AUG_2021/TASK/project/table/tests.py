import unittest

from project.table.inside_table import InsideTable


class TestTable(unittest.TestCase):
    def setUp(self) -> None:
        self.test = InsideTable(15, 4)

