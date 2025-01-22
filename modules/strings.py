"""strings.py has the content for module 2 of the PCAP course on Udemy"""
import logging
import re

from modules.utils.decorator import Decorator


def basics():
    print(ord('A'))
    print(ord('d'))
    print(ord('a'))
    print(chr(40))
    print(ord('('))
    multi_line = """tewst
    aaa"""
    print(multi_line)
    print(len(multi_line))
    print(len('single_line'))
    # space is the lowest code
    print(min(multi_line))
    print(min("abcdefgh"))
    print(max(multi_line))
    print(float('1.1'))


def searching():
    multi_line = """tewst
    aaa"""
    print(multi_line.index(' '))
    print("test_module".index('t'))
    # gets the first letter index
    print("test_module".index('te'))

    # ValueError: 'te' is not in list
    # print(["test_module"].index('te'))
    print(["test_module", "te", "ta"].index('ta'))

    # ValueError: substring not found
    # print("test_module".index('x'))
    # returns -1
    print("\nString.find function:\n")
    word = 'a'
    word_re = r'\barg\b'.replace('arg', word)
    print(re.findall(word_re, "A a abcd agora e o brasil", re.IGNORECASE))
    logging.log(logging.INFO, "")
    print("test_module".find('x'))
    print("test_module".index('s'))
    print("test_module".find('s'))
    print("find with start")
    print("test_module python".find('s', 5))
    print("test_module python".find(' ', 4))

    print("test_module python".find('p', 5, 8))
    print("test_module python".find('p', 6, 8))

    print("test_module python".find('t'))
    print("rfind")
    print("test_module python".rfind('t'))
    print("test_module python".rfind('n', 6))
    print("test_module python".rfind('n', 6, 10))

    # all invalid indexes
    print("test_module python".find('n', 10, 6))
    print("test_module python".find('t', 10, 0))
    print("test_module python".rfind('n', 10, 6))
    print("test_module python".rfind('t', 10, 0))
    print("rfind with negative index")
    print("test_module python".rfind('d', -12, 10))
    print("test_module python"[-12:10])

    print("test_module python".isalnum())
    print("12345678".isalnum())
    print("1234 5678".isalnum())
    print("".isalnum())
    print("a\na".isalnum())
    print("a'a".isalnum())
    print("apostrophe")
    print("a\'a".isalnum())
    print("a_a".isalnum())

    print("Marco".isalpha())
    print("Marco A".isalpha())
    print("Marco7".isalpha())
    print("Marco7".isdigit())
    print("7777".isdigit())
    print("7777".islower())
    print("a".islower())
    print("a a".islower())
    print("a A".islower())
    print(" ".isspace())
    print("\n".isspace())
    print("\t".isspace())


def join_split_sort():
    string = "".join(["Teste", "da", "minha", "String"])
    print(string)

    string = "\n".join(["Teste", "da", "minha", "String"])
    print(string)

    string = " ".join(["Teste", "da", "minha", "String"])
    print(string)

    string = "Teste\nda\tminha String".split()
    print(string)

    string = "Teste\nda\tminha  String".split()
    print(string)

    string = "Teste\nda\tminha  String, a".split()
    print(string)

    string = "Teste\nda\tminha  String, a I'm alive.".split()
    print(string)

    string_sorted = sorted(string)
    print(string_sorted)
    print(string)

    string_sorted = string.sort()
    print(string_sorted)
    print(string)

    string.sort(reverse=True)
    print(string)

    print(sorted(string, reverse=True))

    # TypeError: '<' not supported between instances of 'int' and 'str'
    # letters = ["D", 4, "d", "A", 1, "a", "C", 3, "c", "B", 2, "b"]
    letters = ["D", "4", "d", "A", "1", "a", "C", "3", "c", "B", "2", "b", "@", "#", "$", "*", "&"]
    print(sorted(letters))
    letters.sort(reverse=True)
    print(letters)

    letters = ["D", "4", "d", "A", "1", "a", "C", "3", "c", "B", "2", "b"]
    print(sorted(letters))
    letters.sort()
    print(letters)
    print(ord('1'))
    print(ord('@'))
    print(ord('A'))
    print(ord('a'))
    print(ord('ç'))


def comparisons():
    boolean = 1 == 1
    print(boolean)

    boolean = 100000000000 == 100000000000
    print(boolean)

    boolean = 'Python' == 'Python'
    print(boolean)

    boolean = 'Python' == 'python'
    print(boolean)

    # uppercase has a lower ASCII code value than lowercase
    boolean = 'Python' < 'python'
    print(boolean)

    boolean = '8ython' < 'Python'
    print(boolean)

    # when equal longest is greater
    boolean = 'python' < 'pytho'
    print(boolean)

    # when not equal checks ASCII code
    boolean = 'Python' < 'pytho'
    print(boolean)

    # when not equal checks ASCII code, size doesn't matter
    boolean = 'ABCDEFGH' < 'ZWX'
    print(boolean)

    # when not equal checks ASCII code, size doesn't matter
    boolean = '20' < '8'
    print(boolean)


def execute():
    Decorator.execute_lesson(basics, "Basics")

    Decorator.execute_lesson(searching, "Searching")

    Decorator.execute_lesson(join_split_sort, "Join, Split, Sort")

    Decorator.execute_lesson(comparisons, "Comparisons")


if __name__ == '__main__':
    Decorator.execute_module(execute, "Strings")
