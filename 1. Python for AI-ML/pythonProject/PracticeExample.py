# Python program to illustrate
# function with main
import math


def getInteger():
    result = int(input("Enter integer: "))
    return result


def Main():
    print("Started")
    num = -85

    # fabs is used to get the absolute
    # value of a decimal
    num = math.fabs(num)
    print(num)

    # calling the getInteger function and
    # storing its returned value in the output variable
    output = getInteger()
    print(output)
    for step in range(output):
        print(step)


def Main1():
    myset = set(["Geeks", "For", "Geeks"])
    print(myset)

    step = 0
    while step < 5:
        print(step)
        step = step + 1

    print(False == 0)
    print(True == 1)

    print(True + True + True)
    print(True + False + False)

    print(None == 0)
    print(None == [])


def Main2():
    for i in range(10):

        print(i, end=" ")

        # break the loop as soon it sees 6
        if i == 6:
            break


def fun():
    S = 0

    for i in range(10):
        S += i
        yield S


class Dog:
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"


for i in fun():
    print(i)

# now we are required to tell Python
# for 'Main' function existence
if __name__ == "__main__":
    # Lambda keyword
    g = lambda x: x * x * x

    print(g(7))
    # d = Dog()
    # d.attr2 = "Jaffa"
    # print(d.attr2)
    # fun()
