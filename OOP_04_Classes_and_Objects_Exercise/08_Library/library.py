from typing import List, Dict
from user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str: [str]] = {}  # {autor: [book1, book2,...],...}
        self.rented_books: Dict[str: {str: int}] = {}  # {usernames: {book names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}

            self.rented_books[user.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        try:
            rented = self.rented_books[user.username][book_name]
            return (f'The book "{book_name}" is already rented and will be available in '
                    f'{rented} days!')
        except KeyError:
            pass

    def return_book(self, author: str, book_name: str, user: User) -> str:
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        self.books_available[author].append(book_name)
        del self.rented_books[user.username][book_name]
        user.books.remove(book_name)
