class Car():
    def __init__(self, model, color, initial_speed=0):
        self.model = model
        self.color = color
        if initial_speed < 0:
            self.__speed = 0
        else:
            self.__speed = initial_speed

    def speed_up(self):
        self.__speed += 5

    def slow_down(self):
        if self.__speed < 5:
            self.__speed = 0
        else:
            self.__speed -= 5

    def show_speed(self):
        return f'Current speed: {self.__speed}'