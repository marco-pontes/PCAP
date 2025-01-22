class Programmer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.__format_names()

    def __format_names(self):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()

    def __str__(self):
        return f'programmer={self.first_name} {self.last_name}'