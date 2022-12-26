# Python Practice - Session 5

from collections import Counter
from innerenclosedfunction import outer_func1, outer_func2, outer_func3
import csv

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("\nPython Practice - Session 5")
print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


### Task 5.1
# Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file called `sorted_names.txt`.
# Each name should start with a new line as in the following example:
# Adele
# Adrienne
# ...
# Willodean
# Xavier

def sorting(filename):
    infile = open(filename)
    words = []
    for line in infile:
        temp = line.split()
        for i in temp:
            words.append(i)
    infile.close()
    words.sort()
    print(words)
    outfile = open("data/sorted_names", "w")
    for i in words:
        outfile.writelines(i)
        outfile.writelines("\n")
    outfile.close()


print(
    f" Task 5.1: Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file "
    f"called `sorted_names.txt`. Each name should start with a new line")

sorting("data/unsorted_names.txt")

print("\n-----------------------------------------------------------------------------------")


# Task 5.2
# Implement a function which search for most common words in the file.
# Use `data/lorem_ipsum.txt` file as a example.
# def most_common_words(filepath, number_of_words=3):
#   pass
# print(most_common_words('lorem_ipsum.txt'))
# >>> ['donec', 'etiam', 'aliquam']
# > NOTE: Remember about dots, commas, capital letters etc.

def most_common_words(filepath, number_of_words=3):
    infile = open(filepath)
    words = []
    for line in infile:
        temp = line.split()
        for i in temp:
            words.append(i)
    infile.close()
    words.sort()

    counter_elements = set()
    dict_items = Counter(words)
    for key in words:
        if dict_items[key] > number_of_words - 1:
            counter_elements.add(key)

    print(counter_elements)


print(f" Task 5.2: Implement a function which search for most common words in the file.")
most_common_words("data/most_common_words.txt")
print("\n-----------------------------------------------------------------------------------")


# Task 5.3 File `data/students.csv` stores information about students in [CSV](
# https://en.wikipedia.org/wiki/Comma-separated_values) format. This file contains the student’s names,
# age and average mark. 1) Implement a function which receives file path and returns names of top performer students
# def get_top_performers(file_path, number_of_top_students=5): pass print(get_top_performers("students.csv")) >>> [
# 'Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']

# opening the CSV file
def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path, mode='r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        rows = sorted(reader, key=lambda x: int(x[2]), reverse=True)
        print(rows[0:number_of_top_students])


def descending_order_of_age(file_path, number_of_top_students=5):
    with open(file_path, mode='r') as csvfile:
        reader = csv.reader(csvfile)
        rows = sorted(reader, key=lambda x: int(x[1]), reverse=True)
        outfile = open("data/sorted_age", "w", newline='')
        obj = csv.writer(outfile)
        obj.writerows(rows)


print(f" Task 5.3.1: This file contains the student’s names, age and average mark.")
get_top_performers("data/students.csv")

print(
    f" Task 5.3.2: Implement a function which receives the file path with students info and writes CSV student information to the new file in descending order of age.")
descending_order_of_age("data/students.csv")
print("\n-----------------------------------------------------------------------------------")

# Task 5.4
# Look through file `modules/innerenclosedfunction.py`.
# 1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.
# 2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.
# 2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.

print(f" Task 5.4.1: Find a way to call `inner_function` without moving it from inside of `enclosed_function`.")
outer_func1()
print(f" Task 5.4.2: Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.")
outer_func2()
print(f" Task 5.4.3: Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.")
outer_func3()

print("\n-----------------------------------------------------------------------------------")


# Task 5.5
# Implement a decorator `remember_result` which remembers last result of function it decorates and prints it before next call.
# @remember_result
# def sum_list(*args):
# 	result = ""
# 	for item in args:
# 		result += item
# 	print(f"Current result = '{result}'")
# 	return result

# sum_list("a", "b")
# >>> "Last result = 'None'"
# >>> "Current result = 'ab'"
# sum_list("abc", "cde")
# >>> "Last result = 'ab'"
# >>> "Current result = 'abccde'"
# sum_list(3, 4, 5)
# >>> "Last result = 'abccde'"
# >>> "Current result = '12'"

def historic_results(func):
    # retrive historic outputs from hitoric_outputs.txt file if it exists


    def inner(*args, **kwargs):
        with open('data/historic_outputs.txt', "r") as f:
            previous_outputs = f.readlines()
        for item in previous_outputs: print("Previous Result:", item)

        # append the output in the historic outputs txt file
        with open('data/historic_outputs.txt', 'a') as f:
            f.write("\n" + func(*args, **kwargs))

        print("New Result", func(*args, **kwargs))

        return func(*args, **kwargs)

    return inner


@historic_results
def summarize(*args):
    result = ""
    for i in args:
        result += i
    return result


print(f" Task 5.5: Implement a decorator `remember_result` which remembers last result of function it decorates and "
      f"prints it before next call.")
summarize("a", "b")
print("\n -----------------")
summarize("abc", "cde")
print("\n -----------------")
summarize("Ami", "ne")

print("\n-----------------------------------------------------------------------------------")


# Task 5.6
# Implement a decorator `call_once` which runs a function or method once and caches the result.
# All consecutive calls to this function should return cached result no matter the arguments.
# @call_once
# def sum_of_numbers(a, b):
#     return a + b

# print(sum_of_numbers(13, 42))
# >>> 55
# print(sum_of_numbers(999, 100))
# >>> 55
# print(sum_of_numbers(134, 412))
# >>> 55
# print(sum_of_numbers(856, 232))
# >>> 55

def hello_decorator(func):
    def inner1(*args, **kwargs):
        with open('data/same_outputs.txt', "r") as f:
            previous_outputs = f.readlines()

        if len(previous_outputs) == 0:
            with open('data/same_outputs.txt', 'a') as f:
                returned_value = func(*args, **kwargs)
                f.write(str(returned_value))
        else:
            returned_value = previous_outputs
            # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    return a + b


print(f" Task 5.6: Implement a decorator `call_once` which runs a function or method once and caches the result. "
      f"All consecutive calls to this function should return cached result no matter the arguments.")
print(sum_two_numbers(1, 10))
print(sum_two_numbers(1, 5))
print(sum_two_numbers(999, 100))

print("\n-----------------------------------------------------------------------------------")



# Task 5.7*
# Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.
# Try to change x to a list `[1,2,3]`. Explain the result.
# Try to change import to `from x import *` where x - module names. Explain the result.


print(f" Task 5.7: Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.")


print("\n-----------------------------------------------------------------------------------")
