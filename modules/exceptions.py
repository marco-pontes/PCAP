"""exeptions.py has the content for the Exceptions module in the PCAP course on Udemy"""
import sys
from enum import Enum


class EmptyGameRulesError(ValueError):
    pass


class InvalidNumberOfCardsErrorUsingExceptionTupleMessage(Exception):
    def __init__(self, number=-1, *args):
        super().__init__(args)
        self.number = number

    """" the implementation below is the same as not having the __str__ method"""

    def __str__(self):
        return super().__str__()


class InvalidNumberOfCardsError(Exception):
    def __init__(self, number=-1, message=''):
        super().__init__()
        self.number = number
        self.message = message

    """" the implementation below is the same as not having the __str__ method"""

    def __str__(self):
        return f'{type(self).__name__}::: {self.message}'


class ActivityType(Enum):
    INDOORS = "INDOORS"
    OUTDOORS = "OUTDOORS"


class GroupActivity:
    count = 0

    def __init__(self, name, kind):
        self.name = name
        self.type = kind


class Game(GroupActivity):
    count = 1

    def __init__(self, name, kind, rules):
        super().__init__(name, kind)
        if not rules:
            raise EmptyGameRulesError("The game must have at least one rule", 1, 3)
        self.rules = rules


class BoardGame(Game):
    def __init__(self, name, kind, rules, cards):
        if cards < 0 or cards > 999:
            raise InvalidNumberOfCardsErrorUsingExceptionTupleMessage(cards, "Message passed as generic args to the Exception class")
        if cards == 998:
            raise InvalidNumberOfCardsError(cards, "Message as a property in my exception class")
        super().__init__(name, kind, rules)
        self.cards = cards

    def present_rules(self):
        return 'Regras do Board Game: \n' + '\n'.join(self.rules)


def basics():
    print("=" * 40 + " Basics " + "=" * 40 + "\n")

    try:
        int("a")
    except ValueError:
        print("ValueError: tried to convert a string to int")

    try:
        1 / 0
    except ZeroDivisionError:
        print("ZeroDivisionError: tried to divide by zero")

    try:
        sys.exit()
    except SystemExit:
        print("SystemExit")

    # ['a'][1]
    # IndexError: list index out of range

    # (1, 3).test = 2
    # AttributeError: 'tuple' object has no attribute 'test'

    # a = 1
    # a.append(1)
    # AttributeError: 'int' object has no attribute 'append'

    # { 'a': 2 }['b']
    # KeyError: 'b'

    # int("a")
    # ValueError: invalid literal for int() with base 10: 'a'

    # a.b
    # NameError: name 'a' is not defined

    # a()
    # NameError: name 'a' is not defined

    # sorted(3)
    # TypeError: 'int' object is not iterable

    # 10 + ""
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    # "" + 10
    # TypeError: can only concatenate str (not "int") to str
    # 5 < "4"
    # TypeError: '<' not supported between instances of 'int' and 'str'

    print("=" * 40 + " End " + "=" * 50 + "\n\n")


def hierarchy():
    print("=" * 40 + " Hierarchy " + "=" * 40 + "\n")

    # not descendant from Exception:
    print(isinstance(SystemExit(), Exception))
    print(isinstance(KeyboardInterrupt(), Exception))

    # direct descendants from BaseException instead
    print(isinstance(SystemExit(), BaseException))
    print(isinstance(KeyboardInterrupt(), BaseException))

    # Descendants from Exception
    print(isinstance(ValueError(), Exception))
    print(isinstance(TypeError(), Exception))
    print(isinstance(AttributeError(), Exception))

    print(isinstance(Exception(), BaseException))

    print(isinstance(SyntaxError(), Exception))

    print(isinstance(ArithmeticError(), Exception))
    print(isinstance(ZeroDivisionError(), ArithmeticError))

    print(isinstance(LookupError(), Exception))
    print(isinstance(KeyError(), LookupError))
    print(isinstance(IndexError(), LookupError))

    print("BaseException Subclasses:")
    for subclass in BaseException.__subclasses__():
        print(subclass.__name__)

    print("Exception Subclasses:")
    for subclass in Exception.__subclasses__():
        print(subclass.__name__)

    print("=" * 40 + " End " + "=" * 50 + "\n\n")


def exception_finally():
    print("=" * 40 + " Finally " + "=" * 40 + "\n")

    try:
        1 / 0
    except:
        print("Exception occurred")
    else:
        print("No exception occurred")
    finally:
        print("After exception")

    print("Outside try")

    try:
        pass
    except:
        print("Exception occurred")
    else:
        print("No exception occurred")
    finally:
        print("After exception")

    print("Outside try")

    print("=" * 40 + " End " + "=" * 50 + "\n\n")


def function(n, d):
    if not isinstance(n, int):
        raise TypeError("The function needs an integer parameter, but got", n)
    try:
        result = n / d
    except:
        print("Something wrong happened but I'm not treating it here so I'll raise")
        raise


def exception_raising():
    print("=" * 40 + " Exception Raising " + "=" * 40 + "\n")

    try:
        function("1", 1)
    except TypeError as e:
        # TypeError: ('The function needs an integer parameter, but got', '1')
        print("Tratando o type error")
        print(e)
        print(e.args)
        print(type(e.args))

    try:
        function(1, 0)
    except ZeroDivisionError:
        print("Treating the reraised ZeroDivisionError")

    try:
        function(1, 0)
    except ZeroDivisionError as e:
        print("Treating the reraised ZeroDivisionError")
        print(e)
        print(e.args)

    print("=" * 40 + " End " + "=" * 50 + "\n\n")


def creating_an_exception():
    print("=" * 40 + " Creating an Exception " + "=" * 40 + "\n")

    try:
        BoardGame("Sintonia", ActivityType.INDOORS, [], 100)
    except EmptyGameRulesError as e:
        # __main__.EmptyGameRulesError: ('The game must have at least one rule', 1, 3)
        print("Tratando o EmptyGameRulesError")
        print(e)
        print(e.args)
        print(type(e.args))

    try:
        BoardGame("Sintonia", ActivityType.INDOORS, [], 1000)
    except InvalidNumberOfCardsErrorUsingExceptionTupleMessage as e:
        print("Tratando o InvalidNumberOfCardsErrorUsingExceptionTupleMessage")
        print(e)
        print(e.args)
        print(type(e.args))

    try:
        BoardGame("Sintonia", ActivityType.INDOORS, [], 998)
    except InvalidNumberOfCardsError as e:
        print("Tratando o InvalidNumberOfCardsError")
        print(e)
        print(e.args)
        print(type(e.args))

    print("=" * 40 + " End " + "=" * 50 + "\n\n")


def execute():
    print("_" * 100 + " Exceptions " + "_" * 100 + "\n")

    basics()

    hierarchy()

    exception_finally()

    exception_raising()

    creating_an_exception()

    print("_" * 100 + " End Module " + "_" * 100 + "\n\n")


if __name__ == '__main__':
    execute()
