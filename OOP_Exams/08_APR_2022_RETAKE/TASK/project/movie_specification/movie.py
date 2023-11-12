from abc import ABC, abstractmethod

from project.user import User


class Movie(ABC):
    PEGI_RATED = {"Fantasy": 6, "Action": 12, "Thriller": 16}

    @abstractmethod
    def __init__(self, title: str, year: int, owner: User, age_restriction: int):
        self.title = title
        self.year = year
        self.owner: User = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def type(self):
        return self.__class__.__name__

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value: int):
        if value < Movie.PEGI_RATED[self.type]:
            raise ValueError(
                f"{self.type} movies must be restricted for audience under {Movie.PEGI_RATED[self.type]} years!")
        self.__age_restriction = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value: str):
        if value == '':
            raise ValueError("The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value: int):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value: User):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")
        self.__owner = value

    def details(self):
        return (f"{self.__class__.__name__} - Title:{self.title}, "
                f"Year:{self.year}, "
                f"Age restriction:{self.age_restriction}, "
                f"Likes:{self.likes}, "
                f"Owned by:{self.owner.username}")
