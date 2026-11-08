from patterns import Singleton
from exceptions import BookNotFoundError


class LibraryDatabase(
    metaclass=Singleton
):

    def __init__(self):

        self.books = []

    def add_book(self, book):

        self.books.append(book)

    def get_books(self):

        return self.books

    def find_book(self, title):

        for book in self.books:

            if book.title == title:

                return book

        raise BookNotFoundError(
            "Книгу не знайдено"
        )

    def remove_book(self, title):

        book = self.find_book(title)

        self.books.remove(book)
