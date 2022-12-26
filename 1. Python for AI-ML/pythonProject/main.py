# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

a = True
b = 1 if a else 0
print(b)


def findLen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter


str = "geeks geeks"
print(findLen(str))


dogs= ['Gus', 'Bubba', 'Snoopy']

animals = []

animals = [f'Dog {dog}' for dog in dogs]


print(animals)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
