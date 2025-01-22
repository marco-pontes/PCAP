"""miscellaneous.py has the content for module Miscellaneous of the PCAP course on Udemy"""
import os
import random
import sys
from modules.utils.decorator import Decorator


def apply_func(func, *args):
    return print(func(*args))




def list_comprehensions_advanced():
    numbers = [i for i in range(1, 101)]
    print(numbers)

    numbers = [i for i in range(1, 101) if i % 2 == 0]
    print(numbers)

    numbers = [0 if i % 2 == 0 else 1 for i in range(1, 101)]
    print(numbers)

    numbers = [[i for i in range(1, 11)] for j in range(10, 20)]
    print(numbers)


def lambda_functions():
    sumbda = lambda a, b: a + b
    print(sumbda(2, 4))

    def sumbda_b(a, b): return a + b

    print(sumbda_b(4, 4))

    prinbda = lambda a, b: print(a + b)
    prinbda(8, 8)

    apply_func(sumbda, 5, 5)


def map_filter_advanced():
    numbers = [1, 2, 3, 4, 5]
    emails = ['asdasdsad', 'test@test.com', '234234523423', 'test@gmail.com']
    result = map(lambda x: x + 10, numbers)
    result2 = filter(lambda _: random.choice([False, True]), numbers)
    result3 = filter(lambda e: '@' in e, emails)
    print(list(result))
    print(list(result2))
    print(list(result3))


def closures():
    def get_number(number):
        def inner_func():
            # closure because it references the outer variable, otherwise it would be just a nested function
            return number * 100

        return inner_func

    test = get_number(999)
    # the number variable is a free variable inside test function
    print(test())

    def make_multiply_closure(x):
        def multiply_closure(y):
            return x * y

        return multiply_closure

    hundred_multiply = make_multiply_closure(100)
    ten_multiply = make_multiply_closure(10)

    print(hundred_multiply(5))
    print(hundred_multiply(9))
    print(ten_multiply(2))
    print(ten_multiply(4))


def text_files():
    stream = None
    try:
        stream = open('./files/example.txt')
        print(stream.read(5))
        print(stream.read())
    except IOError as e:
        print('Error Writing to file:: ', e)
    finally:
        stream.close()

    try:
        stream = open('./files/text.txt')
        try:
            print(stream.read())
        finally:
            stream.close()
    except IOError as e:
        print(e)

    try:
        with open('./files/example.txt', 'a+') as out:
            out.write('Written programmatically\n')
    except IOError as e:
        print(e)
    finally:
        out.close()

    try:
        with open('./files/example.txt', 'r') as out:
            character = out.read(1)
            counter = 0
            while character != '':
                print(character, end='-')
                counter += 1
                character = out.read(1)
            print(f'\nNumber of characters: {counter}\n')
    except IOError as e:
        print(e)
    finally:
        out.close()

    try:
        with open('./files/games.txt', 'r') as out:
            line = out.readline()
            counter = 0
            while line != '':
                sys.stdout.write(line)
                counter += 1
                line = out.readline()
            print(f'\nNumber of lines: {counter}\n')
    except IOError as e:
        print(e)
    finally:
        out.close()

    try:
        with open('./files/board-games.txt', 'r') as out:
            lines = out.readlines()
            print(f'\nLines var content: {lines}\n')
            print(f'\nNumber of lines: {len(lines)}\n')
            for line in lines:
                print(line)
    except IOError as e:
        print(e)
    finally:
        out.close()

    try:
        with open('./files/games.txt', 'r') as out:
            for line in out:
                print(line)
    except IOError as e:
        print(e)


def binary_files():
    data = bytearray(100)
    data[0] = 100
    data[1] = 120
    data[2] = 235
    try:
        with open('./files/file.bin', 'wb') as stream:
            stream.write(data)
    except IOError as e:
        print(e)
    finally:
        stream.close()

    try:
        with open('./files/file.bin', 'rb') as stream:
            byte_array = stream.read()
            print(byte_array)
            for byte in byte_array:
                print(hex(byte), end=' ')
            print()
            for byte in byte_array:
                print(int(byte), end=' ')
    except IOError as e:
        print(e)
    finally:
        stream.close()

    try:
        with open('./files/file.bin', 'rb') as stream:
            byte_array = stream.read(10)
            print()
            print(type(byte_array))
            for byte in byte_array:
                print(int(byte), end=' ')
            print()
    except IOError as e:
        print(e)
    finally:
        stream.close()

    try:
        with open('./files/file.bin', 'rb') as stream:
            byte_array = bytearray(stream.read(10))
            print(type(byte_array))
            print()
    except IOError as e:
        print(e)
    finally:
        stream.close()

    byte_array_2 = bytearray(10)
    try:
        with open('./files/file.bin', 'rb') as stream:
            stream.readinto(byte_array_2)
            print(type(byte_array_2))
            print(byte_array_2)
            print()
    except IOError as e:
        print(e)
    finally:
        stream.close()


def file_modes():
    try:
        with open('./files/doesnt-exist.txt', 'r') as out:
            for line in out:
                print(line)
    except IOError as e:
        print(e)

    try:
        with open('./files/doesnt-exist2.txt', 'w') as out:
            #w erases the file and write again, creates the file if doesnt exist
            out.write("Teste2")
    except IOError as e:
        print(e)

    try:
        with open('./files/doesnt-exist3.txt', 'a') as out:
            #a creates the file, and updates it without wiping content
            out.write("Teste2")
    except IOError as e:
        print(e)

    try:
        with open('./files/doesnt-exist4.txt', 'x') as out:
            #x creates the file, and throws error in case it already exists
            out.write("Teste2")
    except IOError as e:
        print(e)
        
    try:
        with open('./files/example.txt', 'a') as out:
            #x creates the file, and throws error in case it already exists
            for line in out:
                print(line)
    except IOError as e:
        print(e)

    try:
        with open('./files/example.txt', 'w') as out:
            #x creates the file, and throws error in case it already exists
            for line in out:
                print(line)
    except IOError as e:
        print(e)

    filename = './files/new.txt'
    try:
        with open(filename, 'x') as out:
            #x creates the file, and throws error in case it already exists
            for line in out:
                print(line)
    except IOError as e:
        print(e)
    finally:
        os.remove(filename)

    # the plus(+) sign adds read mode to a, w and x


def predefined_streams():
    # for a in sys.stdin:
    #     print(a)
    sys.stdout.write("Testezinho")
    # TypeError
    #sys.stdout.write(3)
    sys.stdout.write(str(3))
    sys.stdout.write("\n")
    sys.stderr.write("Erro?")
    # TypeError
    #sys.stderr.write(3)

def error_numbers():
    try:
        with open('./files/example.txt', 'x') as out:
            #x creates the file, and throws error in case it already exists
            for line in out:
                print(line)
    except IOError as e:
        print(os.strerror(e.errno))
        print(e.errno)


def execute():
    Decorator.execute_lesson(list_comprehensions_advanced, "List Comprehensions Advanced")

    Decorator.execute_lesson(lambda_functions, "Lambda Functions")

    Decorator.execute_lesson(map_filter_advanced, "Map Filter Advanced")

    Decorator.execute_lesson(closures, "Closures")

    Decorator.execute_lesson(text_files, "Text Files")

    Decorator.execute_lesson(binary_files, "Binary Files")

    Decorator.execute_lesson(file_modes, "File Modes")

    Decorator.execute_lesson(predefined_streams, "Predefined Streams")

    Decorator.execute_lesson(error_numbers, "Error Numbers")

if __name__ == '__main__':
    Decorator.execute_module(execute, "Miscellaneous")
