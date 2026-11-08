from functools import wraps


def validate_string(func):

    @wraps(func)
    def wrapper(self, *args, **kwargs):

        for arg in args:

            if not isinstance(arg, str):

                raise ValueError(
                    "Значення повинне бути рядком"
                )

            if not arg.strip():

                raise ValueError(
                    "Порожній рядок заборонений"
                )

        return func(
            self,
            *args,
            **kwargs
        )

    return wrapper
