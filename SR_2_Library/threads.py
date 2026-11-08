import threading


def search_book(database, title):

    try:

        book = database.find_book(
            title
        )

        print(
            f"[THREAD] "
            f"Знайдено книгу: {book}"
        )

    except Exception as error:

        print(
            f"Помилка: {error}"
        )


def run_threads(database):

    thread1 = threading.Thread(
        target=search_book,
        args=(
            database,
            "Python"
        )
    )

    thread2 = threading.Thread(
        target=search_book,
        args=(
            database,
            "Java"
        )
    )

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
