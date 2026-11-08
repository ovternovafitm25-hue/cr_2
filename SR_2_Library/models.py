from metaclasses import LoggingMeta
from decorators import validate_string


class Author(metaclass=LoggingMeta):

    @validate_string
    def __init__(self, name):

        self.name = name

    def __str__(self):

        return self.name


class Book(metaclass=LoggingMeta):

    def __init__(self, title, author):

        if not isinstance(title, str):
            raise ValueError(
                "Назва книги повинна бути рядком"
            )

        self.title = title
        self.author = author


    def __str__(self):

        return (
            f"{self.title} - "
            f"{self.author}"
        )


class Reader(metaclass=LoggingMeta):

    @validate_string
    def __init__(self, name):

        self.name = name

    def __str__(self):

        return self.name
