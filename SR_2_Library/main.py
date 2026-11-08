from models import Author
from models import Book
from models import Reader

from database import LibraryDatabase

from threads import run_threads


def main():

    author1 = Author(
        "Тарас Шевченко"
    )

    author2 = Author(
        "Леся Українка"
    )

    book1 = Book(
        "Python",
        author1
    )

    book2 = Book(
        "Java",
        author2
    )

    reader = Reader(
        "Ольга"
    )

    db = LibraryDatabase()

    db.add_book(book1)
    db.add_book(book2)

    print()

    print(
        "Список книг у бібліотеці"
    )

    for book in db.get_books():

        print(book)

    print()

    run_threads(db)

    print()

    print(
        "Читач:"
    )

    print(reader)


if __name__ == "__main__":
    main()
