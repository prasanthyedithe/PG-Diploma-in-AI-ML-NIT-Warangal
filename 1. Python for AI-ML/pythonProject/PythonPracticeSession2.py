# Python Practice - Session 2
from collections import Counter

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("\nPython Practice - Session 2")
print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


# Task 2.1
# Write a Python program to calculate the length of a string without using the `len` function.

def find_length_of_string(input: object) -> object:
    counter = 0
    for i in input:
        counter += 1
    return counter


input_char_parm = "geeks"
print(f" \n Task 2.1 : Length of a string {input_char_parm} is : ", find_length_of_string(input_char_parm))
print("\n-----------------------------------------------------------------------------------")
# Task 2.2
# Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
# Examples:
# Input: 'Oh, it is python'
# Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}

input_string_param = 'Oh, it is python'
print(f" \n Task 2.2 : Number of characters in string {input_string_param} is : ", Counter(input_string_param))
print("\n-----------------------------------------------------------------------------------")

# Task 2.3
# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
# Examples:
# Input: ['red', 'white', 'black', 'red', 'green', 'black']
# Output: ['black', 'green', 'red', 'white']

input_list_param = ['red', 'white', 'black', 'red', 'green', 'black']
sorted_input_list = sorted(set(input_list_param))
print(f" \n Task 2.3 : Sorted List for Input List {input_list_param} is : ", sorted_input_list)
print("\n-----------------------------------------------------------------------------------")


# Task 2.4
# Create a program that asks the user for a number and then prints out a list of all the [divisors] of that number.
# Examples:
# Input: 60
# Output: [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]

def divisors_of_number(input_number: object) -> object:
    i = 1
    input_number_list = []
    while i <= input_number:
        if input_number % i == 0:
            input_number_list.append(i)
        i += 1
    return input_number_list


input_number_param = 60
print(f" \n Task 2.4 : Prints out a list of all the [divisors] of that number {input_number_param} :",
      divisors_of_number(input_number_param))
print("\n-----------------------------------------------------------------------------------")


# Task 2.5
# Write a Python program to sort a dictionary by key.

def sort_dict_by_key(d, reverse=False):
    return dict(sorted(d.items(), reverse=reverse))


color_dict = {'red': '#FF0000', 'green': '#008000', 'black': '#000000', 'white': '#FFFFFF'}
print(f" \n Task 2.5 : Program to sort a dictionary by key {color_dict} :")
print("Sort the said dictionary by key (Ascending order):")
print(sort_dict_by_key(color_dict))
print("Sort the said dictionary by key (Descending order):")
print(sort_dict_by_key(color_dict, True))

print("\n-----------------------------------------------------------------------------------")

# Task 2.6
# Write a Python program to print all unique values of all dictionaries in a list.
# Examples:
# Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Output: ['S005', 'S002', 'S007', 'S001', 'S009']

input_list_dic_param = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                {"VIII": "S007"}]
sorted_value = set(val for dic in input_list_dic_param for val in dic.values())
print(f" \n Task 2.6 : Prints all unique values of all dictionaries in a list {input_list_dic_param} :",
      list(sorted_value))
print("\n-----------------------------------------------------------------------------------")


# Task 2.7
# Write a Python program to convert a given tuple of positive integers into an integer.
# Examples:
# Input: (1, 2, 3, 4)
# Output: 1234

def tuple_into_int(input_tuple):
    result = int(''.join(map(str, input_tuple)))
    return result


input_tuple_param = (1, 2, 3, 4)
print(f" \n Task 2.7 : Convert a given tuple of positive integers into an integer {input_tuple_param} :",
      tuple_into_int(input_tuple_param))
print("\n-----------------------------------------------------------------------------------")

# Task 2.8
# Write a program which makes a pretty print of a part of the multiplication table.
# Examples:
# Input:
# a = 2
# b = 4
# c = 3
# d = 7
# Output:
# 	3	4	5	6	7
# 2	6	8	10	12	14
# 3	9	12	15	18	21
# 4	12	16	20	24	28

print(" \n Task 2.8 : program which makes a pretty print of a part of the multiplication table")
input_integer_param = int(input('Please enter a positive integer greater than 1 : '))
for row in range(1, input_integer_param + 1):
    for col in range(1, input_integer_param + 1):
        if row == 1 and col == 1:
            print("", end="\t")
        else:
            print(row * col, end="\t")
    print()
