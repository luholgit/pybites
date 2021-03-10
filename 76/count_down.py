from functools import singledispatch
from itertools import count


@singledispatch
def count_down(data_type):
    # this triggers only if the data type is not specifically defined below --> raise error
    raise ValueError


@count_down.register(float)
@count_down.register(int)
@count_down.register(str)
def _(arg):
    # convert to string
    arg_str = str(arg)

    while len(arg_str) > 0:
        print(arg_str)
        arg_str = arg_str[:-1]


@count_down.register(list)
@count_down.register(tuple)
@count_down.register(dict)
@count_down.register(set)
@count_down.register(range)
def _(arg_list):
    # concat
    print_list = [str(x) for x in arg_list]

    while len(print_list) > 0:
        print(_join_list(print_list))

        # drop last element
        del print_list[-1]


def _join_list(list_in):
    return "".join(list_in)
