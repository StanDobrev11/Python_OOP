from project.movie_specification.movie import Movie
from project.user import User


class Action(Movie):
    def __init__(self, title: str, year: int, owner: User, age_restriction=12):
        super().__init__(title, year, owner, age_restriction)
