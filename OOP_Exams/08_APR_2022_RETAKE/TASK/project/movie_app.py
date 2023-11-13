from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def get_existing_user(self, username):
        try:
            return [u for u in self.users_collection if u.username == username][0]
        except IndexError:
            return False

    def register_user(self, username: str, age: int):
        user = User(username, age)

        if self.get_existing_user(username):
            raise Exception("User already exists!")

        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        """
        The method adds the movie to the user's movies_owned list as well as the movies_collection list
        Only the owner of the given movie can upload it.
        """
        if not self.get_existing_user(username):
            raise Exception("This user does not exist!")

        user = self.get_existing_user(username)

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        if movie.owner != user:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{user.username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **attrs):  # **kwargs = ("title", "year", or "age_restriction")
        """
        Only the owner of the movie given can edit it.
        You will always be given usernames of registered users.
        """

        user = self.get_existing_user(username)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attr, value in attrs.items():
            setattr(movie, attr, value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):

        user = self.get_existing_user(username)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        """Owners cannot like their own movies"""
        user = self.get_existing_user(username)

        if movie in user.movies_owned:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        """Only the user who has liked the movie can dislike it"""

        user = self.get_existing_user(username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        text = []
        for movie in sorted(self.movies_collection, key=lambda m: (-m.year, m.title)):
            text.append(movie.details())

        if not text:
            return "No movies found."

        return '\n'.join(text)

    def __str__(self):
        line_1 = f"All users: {', '.join(user.username for user in self.users_collection) if self.users_collection else 'No users.'}"
        line_2 = f"All movies: {', '.join(movie.title for movie in self.movies_collection) if self.movies_collection else 'No movies.'}"
        return line_1 + '\n' + line_2
