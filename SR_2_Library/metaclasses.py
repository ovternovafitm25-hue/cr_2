class LoggingMeta(type):

    def __call__(cls, *args, **kwargs):

        print(
            f"[META] Створено об'єкт класу {cls.__name__}"
        )

        return super().__call__(
            *args,
            **kwargs
        )
