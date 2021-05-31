MSG = "Hey {}, there are more people with your birthday!"


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __setitem__(self, name, birthday):

        if f"{birthday.month}-{birthday.day}" in [f"{x.month}-{x.day}" for x in self.values()]:
            print(MSG.format(name))

        self.update({name: birthday})

