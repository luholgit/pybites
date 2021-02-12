from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapped(*args):
        # check if any of the inputs is not of type int
        if not all(isinstance(item, int) for item in args):
            raise TypeError

        # check if any is below 0
        if any(item < 0 for item in args):
            raise ValueError

        # everything's fine return the result
        return func(*args)

    return wrapped

