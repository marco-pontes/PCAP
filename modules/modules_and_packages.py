"""modules_and_packages.py has the content for module 1 of the PCAP course on Udemy"""
import sys
import sys, math
# from sys import *
from sys import exit
from sys import exit as e
import sys as s
import random
import platform
import sys
import test_module.fake_module as t


#from test_module.fake_module import fake_function


def e():
    print("Overwritten the imported e function")


def math_module():
    print("=" * 40 + " Math module " + "=" * 40 + "\n")
    print(math.pi)
    # e()
    for name in dir(math):
        print(name, end='\t')
    print()
    # ceil, floor, trunc
    number = 8.99999999
    print(math.ceil(number))
    print(math.floor(number))
    print(math.trunc(number))
    print()
    number = 8.0
    print(math.ceil(number))
    print(math.floor(number))
    print(math.trunc(number))
    print()
    print(math.factorial(3))  # 3! = 3 * 2 * 1 = 6
    print(math.sqrt(3))
    print(math.sqrt(9))
    # float results for sqrt
    print()
    print(math.hypot(90, 100))
    print("=" * 40 + " End " + "=" * 50 + "\n\n")


def module_paths():
    print("=" * 40 + " Module Paths " + "=" * 40 + "\n")
    print(sys.path)
    # test_module.fake_module.fake_function()
    t.fake_function()
    print("=" * 40 + " End " + "=" * 50 + "\n\n")


def platform_module():
    print("=" * 40 + " Platform Module " + "=" * 40 + "\n")
    print(platform.platform())
    print(platform.platform(False, True))
    print(platform.machine())
    print(platform.processor())
    print(platform.system())
    print(platform.python_implementation())
    print(platform.python_version_tuple())
    print(platform.version())
    print(platform.python_version())
    print("=" * 40 + " End " + "=" * 50 + "\n\n")


def random_module():
    print("=" * 40 + " Random module " + "=" * 40 + "\n")
    print(random.random())
    print(random.random())
    print(random.random())
    random.seed(1)
    print(random.random())
    print(random.random())
    print(random.random())
    random.seed(1)  # this repeats the numbers shown in the first three calls
    print(random.random())
    print(random.random())
    print(random.random())
    random.seed()  # reseting seed
    board_games = ["munshkin", "sintonia", "the mind", "exploding kittens", "war"]
    numbers = [0, 4, 8, 2, 10]
    print(random.choice(board_games))
    print(random.choice(board_games))
    print(random.choice(board_games))
    print()
    for i in range(len(board_games)):  # repeats choices
        print(random.choice(board_games))
    print()
    # get a sample with unique choices
    print(random.sample(board_games, 3))  # parameter can't be larger than list length ValueError
    print("=" * 40 + " End " + "=" * 50 + "\n\n")


def execute():
    print("_" * 100 + " Modules and Packages " + "_" * 100 + "\n")
    math_module()

    random_module()

    platform_module()

    module_paths()

    print("_" * 100 + " End Module " + "_" * 100 + "\n\n")


if __name__ == '__main__':
    execute()
