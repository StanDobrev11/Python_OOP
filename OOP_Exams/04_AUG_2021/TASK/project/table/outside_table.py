from project.table.table import Table


class OutsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self) -> int:
        return self.__table_number

    @table_number.setter
    def table_number(self, value: int) -> None:
        if value not in range(51, 101):
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")
        self.__table_number = value

    @property
    def type(self) -> str:
        return "OutsideTable"
