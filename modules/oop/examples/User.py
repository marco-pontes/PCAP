class User:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def introduce(self):
        return f'Hi, my name is {self.name} from {self.city}'