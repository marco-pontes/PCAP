"""object_orientation.py has the content for module Y of the PCAP course on Udemy"""
from modules.oop.examples.BoardGameClass import BoardGameClass
from modules.oop.examples.Car import Car
from modules.oop.examples.Dog import Dog
from modules.oop.examples.Doggo import Doggo
from modules.oop.examples.House import House
from modules.oop.examples.Programmer import Programmer
from modules.oop.examples.Rectangle import Rectangle
from modules.oop.examples.User import User
from modules.oop.examples.activity.ActivityType import ActivityType
from modules.oop.examples.activity.BoardGame import BoardGame
from modules.oop.examples.activity.Game import Game
from modules.oop.examples.activity.GroupActivity import GroupActivity
from modules.oop.examples.vehicle.Airplane import Airplane
from modules.oop.examples.vehicle.Flyable import Flyable
from modules.oop.examples.vehicle.HybridVehicle import HybridVehicle
from modules.oop.examples.vehicle.Vehicle import Vehicle
from test_module import fake_module
from modules.utils.decorator import Decorator

def change_object(user_object):
    for prop_name in user_object.__dict__.keys():
        value = getattr(user_object, prop_name)
        if isinstance(value, str):
            setattr(user_object, prop_name, '')


def classes_and_objects():
    rectangle = Rectangle(10, 30)
    print("Rectangle area: ", rectangle.get_area())
    print("Rectangle width: ", rectangle.width)

    user = User("Marco", "Joinville")
    print(user.introduce())


def encapsulation_and_abstraction():
    car = Car("Focus", "White")
    car.speed_up()
    car.speed_up()
    print(car.show_speed())

    car = Car("Focus", "White")
    car.slow_down()
    car.slow_down()
    print(car.show_speed())

    car = Car("Focus", "White")
    car.speed = -30
    print(car.show_speed())

    car = Car("Focus", "White")
    car.__speed = -30
    car._Car__speed = - 30
    print(car.show_speed())


def instance_variables():
    dog = Dog("Preta", 10)
    dog.color = "Black"

    del dog.name

    print(dog.__dict__)

    dog = Doggo("Preta", 10)
    dog.color = "Black"
    # it's possible to change :/
    # dog._Doggo__name = "teste"
    # name mangling only works from inside the class
    dog.__size = "Medium"

    print(dog.__dict__)


def class_variables():
    board_game1 = BoardGameClass("Munshkin", 6)
    print(BoardGameClass.counter)
    print(board_game1.counter)
    board_game2 = BoardGameClass("Exploding Kittens", 5)
    print(BoardGameClass.counter)
    print(board_game2.counter)
    print(board_game1.counter)

    print(board_game1.__dict__)
    print(BoardGameClass.__dict__)

    if hasattr(board_game1, 'name'):
        print("Has Name")

    if not hasattr(board_game1, 'namezim'):
        print("Has no property namezim")

    if hasattr(BoardGameClass, '_BoardGameClass__counter'):
        print("Has _BoardGameClass__counter")

    if not hasattr(BoardGameClass, '__counter'):
        print("Doesnt Have __counter")

    print(BoardGameClass.__name__)
    # print(board_game1.__name__)
    # AttributeError: 'BoardGame' object has no attribute '__name__'

    print(type(board_game1))
    print(type(board_game1).__name__)

    print(board_game1.__module__)
    print(BoardGameClass.__module__)
    print(fake_module.fake_function.__module__)
    print(fake_module.FakeClass.__module__)

    house = House('', 400, 400000)

    print(house.present())
    House.quality = 'sdsds'
    print(house.__dict__)
    print(House.__dict__)
    print('test'.title())


def class_methods():
    prog = Programmer('marco', 'pontes')
    print(prog)
    print(prog.__dict__)
    print(Programmer.__dict__)


def introspection_reflection():
    prog = Programmer('marco', 'pontes')
    print(prog.__dict__)
    change_object(prog)
    print(prog.__dict__)

    s = "prog"
    print(s)
    # AttributeError: 'str' object has no attribute '__dict__'
    # change_object(s)
    # AttributeError: 'int' object has no attribute '__dict__'
    # change_object(10)
    # AttributeError: 'bool' object has no attribute '__dict__'
    # change_object(True)
    print(s)


def inheritance():
    print(issubclass(Game, Game))
    print(issubclass(Game, GroupActivity))
    print(issubclass(BoardGame, Game))
    print(issubclass(BoardGame, GroupActivity))
    print(issubclass(GroupActivity, BoardGame))

    board_game = BoardGame("Sintonia", ActivityType.INDOORS, [], 200)
    game = Game("Squash", ActivityType.INDOORS, [])
    activity = GroupActivity("Taekwondo", ActivityType.INDOORS)

    print(board_game.__dict__)
    print(game.__dict__)
    print(activity.__dict__)
    print(Game.__dict__)
    print(GroupActivity.__dict__)
    print(activity.count)
    print(board_game.count)
    board_game.add_rule("Regra 1")
    print(board_game.__dict__)
    print(board_game.present())
    print(game.present())
    print(isinstance(activity, GroupActivity))
    print(isinstance(activity, Game))
    print(isinstance(activity, BoardGame))

    print()

    print(isinstance(game, GroupActivity))
    print(isinstance(game, Game))
    print(isinstance(game, BoardGame))

    print()

    print(isinstance(board_game, GroupActivity))
    print(isinstance(board_game, Game))
    print(isinstance(board_game, BoardGame))

    print(GroupActivity.__bases__)
    print(Game.__bases__)
    print(BoardGame.__bases__)

    print()
    game_reference = game

    print(game_reference is game)
    print()

    first_num = 5
    sec_num = 5
    print(first_num is sec_num)

    first_num = 5
    sec_num = 3
    sec_num += 2
    print(first_num is sec_num)

    first_str = "a"
    sec_str = 'a'
    print(first_str is sec_str)

    first_str = "a"
    sec_str = "b"
    print(first_str is sec_str)

    first_str = "test"
    sec_str = "tes"
    sec_str += 't'
    print(first_str is sec_str)
    print(first_str == sec_str)

    print(str.__bases__)


def multiple_inheritance():
    airplane = Airplane()

    print(isinstance(airplane, Flyable))
    print(isinstance(airplane, Vehicle))
    print(isinstance(airplane, Airplane))

    print(airplane.go())
    print(airplane.fly())
    print(airplane.present())

    print(Airplane.__bases__)

    hybrid_car = HybridVehicle()
    print(hybrid_car.show_power_type())


def execute():
    Decorator.execute_lesson(classes_and_objects, "Classes and Objects")

    Decorator.execute_lesson(encapsulation_and_abstraction, "Encapsulation and Abstraction")

    Decorator.execute_lesson(instance_variables, "Instance Variables")

    Decorator.execute_lesson(class_variables, "Class Variables")

    Decorator.execute_lesson(class_methods, "Class Methods")

    Decorator.execute_lesson(introspection_reflection, "Introspection and Reflection")

    Decorator.execute_lesson(inheritance, "Inheritance")

    Decorator.execute_lesson(multiple_inheritance, "Multiple Inheritance")


if __name__ == '__main__':
    Decorator.execute_module(execute, "Object Orientation")
