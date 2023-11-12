from project.movie_specification.movie import Movie
from project.user import User


class Fantasy(Movie):
    def __init__(self, title: str, year: int, owner: User, age_restriction=6):
        super().__init__(title, year, owner, age_restriction)
