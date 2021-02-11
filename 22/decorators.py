from functools import wraps


def make_html(element):
    def decorater(func):
        def decorated(*args, **kwargs):
            # run actual func
            result = func()

            # add html stuff
            result = f"<{element}>" + result + f"</{element}>"
            return result

        return decorated

    return decorater


# def make_html(func):
#     @wraps(func)
#     def wrapped(element, *args, **kwargs):

#         result = func(*args, **kwargs)

#         return f"<{element}>" + result + f"</{element}>"

#     return wrapped
