from contextlib import contextmanager
from time import time
from datetime import datetime


# Task 7.1 Implement class-based context manager for opening and working with file, including handling exceptions.
# Do not use 'with open()'. Pass filename and mode via constructor.

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


# loading a file
try:
    with FileManager('data/test.txt', 'w') as f:
        f.write('Test')
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
finally:
    # Make sure to close the file after using it
    print(f.closed)


# Task 7.2 Implement context manager for opening and working with file, including handling exceptions with
# @contextmanager decorator.

@contextmanager
def writable_file(file_path, mode):
    file = open(file_path, mode=mode)
    try:
        yield file
    except Exception as exception:
        print(f"An error occurred while writing to the file: {exception}")
    finally:
        file.close()

    print("Successfully written the text")


with writable_file("data/test.txt", "w") as custFileMgr:
    custFileMgr.write("Hello World !!")


# Task 7.3
# Implement decorator with context manager support for writing execution time to log-file. See contextlib module.

@contextmanager
def mock_time():
    global time
    saved_time = datetime.now()
    time = saved_time.strftime("%H:%M:%S")
    print("time:", time)
    file = open("data/test.txt", mode="w")
    file.write(time)
    file.close()
    yield
    time = saved_time


with mock_time():
    print(f"mock_time", datetime.now())


@mock_time()
def decorator_function():
    print(f"decorator_function", datetime.now())


decorator_function()

# Task 7.4
# Implement decorator for supressing exceptions. If exception not occure write log to console.
friends = {"Nguyen": "tacos", "Hannah": "borscht"}


def get_food(friend_name):
    try:
        food = friends[friend_name]
    except KeyError:
        food = "Value Does't Exist so Suppressed the Error"
        friends[friend_name] = food
    return food


print(get_food("1"))


# Task 7.5 Implement a function to check that number is even (number > 3). A number should be passed as a string.
# Throw different exceptions for different situations. Custom exceptions must be derived from custom base exception (
# not Base Exception class).

def even_numner(number_value):
    try:
        if number_value % 2 == 0:
            print("Event Number !!")
            return
    except TypeError:
        print(f"TypeError: Not a proper integer! Try it again")
    except ValueError:
        print(f"ValueError: Please enter a Valid Integer >3")
    finally:
        print()


print("Great, you successfully entered an integer!")

even_numner(4)


# Task 7.6 Create console program for proving Goldbach's conjecture. Program accepts number for input and print
# result. For pressing 'q' program succesfully close. Use function from Task 7.5 for validating input, handle all
# exceptions and print user friendly output.

def is_prime(a):
    for div in range(2, a // 2 + 1):
        if a % div == 0:
            return False
    return True


def goldbach(n):
    try:
        for p1 in range(2, n):
            if is_prime(p1) and is_prime(n - p1):
                p2 = n - p1
                return str(n) + "=" + str(p1) + "+" + str(p2)
    except TypeError:
        print(f"TypeError: Not a proper integer!  it again")
    except ValueError:
        print(f"ValueError: Please enter a Valid Integer >3")
    except Exception as exception:
        print(exception)


print("goldbach(********",goldbach(44))


### Task 7.7
# TODO


# Task 7.8 Implement your custom iterator class called MySquareIterator which gives squares of elements of collection
# it iterates through.

def MySquareIterator(itr):
    for item in itr:
        print(item * 2)


lst = [1, 2, 3, 4, 5]
MySquareIterator(lst)


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: not (x % n > 0) or x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 20:  # Removing tis will go to endless
        print(n)
    else:
        break
# ## Task 7.9 Implement an iterator class EvenRange, which accepts start and end of the interval as an init arguments
# and gives only even numbers during iteration. If user tries to iterate after it gave all possible numbers `Out of
# numbers!` should be printed.
even_numbers_list = []


def EvenRange(start, end):
    # iterating each number in list
    global even_numbers_list
    even_numbers_list
    for num in range(start, end + 1):
        # checking condition
        if num % 2 == 0:
            even_numbers_list.append(num)

    return even_numbers_list


start = 2
end = 10
er1 = EvenRange(start, end)
iterable_obj = iter(er1)
while True:
    try:
        # Iterate by calling next
        item = next(iterable_obj)
        print(item)
    except StopIteration:
        print("Out of numbers!")
        # exception will happen when iteration will over
        break


### Task 7.10
# Implement a generator which will generate odd numbers endlessly.

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: not (x % n > 0) or x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 20:  # Removing tis will go to endless
        print(n)
    else:
        break
