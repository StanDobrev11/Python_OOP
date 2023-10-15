from calendar import month_name
from typing import Tuple


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int) -> None:
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int) -> "DVD":
        creation_month, creation_year = cls.date_validator(date)
        return cls(name, id, creation_year, creation_month, age_restriction)

    @staticmethod
    def date_validator(date: str) -> Tuple[str, int]:
        day, month, year = date.split('.')
        year = int(year)
        month = month_name[int(month)]
        return month, year

    def __repr__(self) -> str:
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) "
                f"has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}")
