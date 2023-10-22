from typing import List


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: List[Book] = []

    def find_book(self, title: str) -> "Book" or None:
        for book in self.books:
            if book.title == title:
                return book

        return None


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page
