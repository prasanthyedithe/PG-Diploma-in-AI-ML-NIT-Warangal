# Python Practice - Session 4
import string
from collections import Counter
from typing import List, Tuple
from zipfile import ZipFile

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("\nPython Practice - Session 4")
print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


# Task 4.1
# Implement a function which receives a string and replaces all `"` symbols
# with `'` and vise versa.

def replace_string(replace_string):
    return replace_string.translate({ord('"'): "'", ord("'"): '"'})


input_args = '"Isn\'t," she said.'
print(
    f" Task 4.1: receives a string and replaces all `\"` symbols with `'` and vise versa of the String : {input_args}")
print(replace_string(input_args))
print("\n-----------------------------------------------------------------------------------")


# Task 4.2
# Write a function that check whether a string is a palindrome or not. Usage of
# any reversing functions is prohibited. To check your implementation you can use
# strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

def famous_palindromes(input_args):
    y = ""
    for i in input_args:
        y = i + y
    if y == input_args:
        print("Yes !!", y, "is Palindrome")
    else:
        print("Ohh !!", y, "is not a Palindrome")


input_parameter = "malayalam"
print(f"Task 4.2: check whether a string is a palindrome or not : {input_parameter}")
famous_palindromes(input_parameter)
print("\n-----------------------------------------------------------------------------------")


# Task 4.3
# Implement a function which works the same as `str.split` method (without using `str.split` itself, ofcourse).

def split(string, delimiters=' \t\n'):
    result = []
    word = ''
    for c in string:
        if c not in delimiters:
            word += c
        elif word:
            result.append(word)
            word = ''

    if word:
        result.append(word)

    return result


print(f"Task 4.3: Implement a function which works the same as `str.split` method (without using `str.split` itself, "
      f"ofcourse)")
print(f" Input Parameter :'duff_beer 4.00'", split('I love Python so much and I am learning now'))
print("\n-----------------------------------------------------------------------------------")


# Task 4.4
# Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
# which splits the `s` string by indexes specified in `indexes`. Wrong indexes must be ignored.
# Examples:
# ```python
# >>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# ["python", "is", "cool", ",", "isn't", "it?"]
# >>> split_by_index("no luck", [42])
# ["no luck"]

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    # parts = [s[:index] for index in indexes]
    indexes.insert(0, 0)
    parts = [s[i:j] for i, j in zip(indexes, indexes[1:] + [None])]
    return parts


print(f"Task 4.4: Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`, "
      f"which splits the `s` string by indexes specified in `indexes`. Wrong indexes must be ignored.)")
print("In put : split_by_index(\"pythoniscool,isn'tit?\", [6, 8, 12, 13, 18]) ",
      split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
print("In put : split_by_index(\"no luck\", [42])", split_by_index("no luck", [42]))
print("\n-----------------------------------------------------------------------------------")


# Task 4.5
# Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple of a given integer's digits.
# Example:
# >>> split_by_index(87178291199)
# (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)

def get_digits(num: int) -> Tuple[int]:
    return tuple(str(num))


print(
    f"Task 4.5: Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple of a given integer's "
    f"digits.")
print(f"Input Parameter is get_digits(87178291199) ::: ", get_digits(87178291199))
print("\n-----------------------------------------------------------------------------------")


# Task 4.6 Implement a function `get_longest_word(s: str) -> str` which returns the longest word in the given string.
# The word can contain any symbols except whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest
# words in the string with a same length return the word that occures first. Example: >>> get_longest_word('Python is
# simple and effective!') 'effective!' >>> get_longest_word('Any pythonista like namespaces a lot.') 'pythonista'

def get_longest_word(sentence):
    longest = max(sentence.split(), key=len)
    print("Longest word is: ", longest)
    print("And its length is: ", len(longest))


# return output_string

input_sentence = 'Any pythonista like namespaces pythonista1 a lot pythonista2'
print(
    f"Task 4.6: Implement a function `get_longest_word(s: str) -> str` which returns the longest word in the given string. {input_sentence}")
get_longest_word(input_sentence)

print("\n-----------------------------------------------------------------------------------")


# Task 4.7
# Implement a function `foo(List[int]) -> List[int]` which, given a list of
# integers, return a new list such that each element at index `i` of the new list
# is the product of all the numbers in the original array except the one at `i`.
# Example:
# >>> foo([1, 2, 3, 4, 5])
# [120, 60, 40, 30, 24]
# >>> foo([3, 2, 1])
# [2, 3, 6]

def foo(num: List[int]) -> List[int]:
    new_nums = []

    for i in num:
        nums_product = 1

        for j in num:
            if j != i:
                nums_product = nums_product * j

        new_nums.append(nums_product)

    return new_nums


print(f"Task 4.7:  Implement a function `foo(List[int]) -> List[int]` which, given a list of integers, return a new "
      f"list such that each element at index `i` of the new list foo([1, 2, 3, 4, 5])")

print(foo([3, 2, 1]))
print("\n-----------------------------------------------------------------------------------")


# Task 4.8
# Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
# of tuples containing pairs of elements. Pairs should be formed as in the
# example. If there is only one element in the list return `None` instead.
# Example:
# >>> get_pairs([1, 2, 3, 8, 9])
# [(1, 2), (2, 3), (3, 8), (8, 9)]
# >>> get_pairs(['need', 'to', 'sleep', 'more'])
# [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]
# >>> get_pairs([1])
# None

def get_pairs(list_of_values: List) -> List[Tuple]:
    new_list_tup = []

    if len(list_of_values) == 1:
        return new_list_tup.append(None)

    for i in range(0, len(list_of_values) - 1):
        tuple_value = (list_of_values[i], list_of_values[i + 1])
        new_list_tup.append(tuple_value)
    return new_list_tup


print(f"Task 4.8: which returns a list of tuples containing pairs of elements. Pairs should be formed as in the "
      f"example. If there is only one element in the list return `None` instead")
list_input_values = ['need', 'to', 'sleep', 'more']
print(f"Input parameter is : {list_input_values}  O/P is :", get_pairs(list_input_values))

print("\n-----------------------------------------------------------------------------------")

# Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:
# 1) characters that appear in all strings
# 2) characters that appear in at least one string
# 3) characters that appear at least in two strings
# 4) characters of alphabet, that were not used in any string
# Note: use `string.ascii_lowercase` for list of alphabet letters
# test_strings = ["hello", "world", "python", ]
# print(test_1_1(*test_strings))
# >>> ('o',)
# print(test_1_2(*test_strings))
# >>> ('d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y',)
# print(test_1_3(*test_strings))
# >>> ('h', 'l', 'o',)
# print(test_1_4(*test_strings))
# >>> ('a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z',)

MAX_CHAR = 26


def char_appear_in_all_strings(strings, lenght_of_string):
    # primary array for common characters
    # we assume all characters are seen before.
    prim = [True] * MAX_CHAR

    # for each strings
    for i in range(lenght_of_string):

        # secondary array for common characters
        # Initially marked false
        sec = [False] * MAX_CHAR

        # for every character of ith strings
        for j in range(len(strings[i])):

            # if character is present in all
            # strings before, mark it.
            if prim[ord(strings[i][j]) - ord('a')]:
                sec[ord(strings[i][j]) -
                    ord('a')] = True

        # copy whole secondary array
        # into primary
        for i in range(MAX_CHAR):
            prim[i] = sec[i]

    # displaying common characters
    for i in range(26):
        if prim[i]:
            print("%c " % (i + ord('a')), end="")


def char_appear_atleast_in_one_strings(strings):
    d = {}

    for val in strings:
        for element in val:
            if element in d.keys():
                d[element] = d[element] + 1
            else:
                d[element] = 1
    return d


def char_appear_atleast_in_two_strings(atleast_two_char):
    list_value = char_appear_atleast_in_one_strings(atleast_two_char)
    list_values = []
    for x, y in list_value.items():
        if y >= 2:
            list_values.append(x)

    return list_values


def char_not_used_strings(strings):
    return set(string.ascii_lowercase) - set(strings)


print(
    f"Task 4.9: Implement a bunch of functions which receive a changeable number of strings and return next parameters")
input_test_string = ["hello", "world", "python", ]
test_strings = list(map(str.lower, input_test_string))
n = len(test_strings)
print(f"1) characters that appear in all strings")
char_appear_in_all_strings(test_strings, n)

print(f"\n2) characters that appear in at least one string")
print(char_appear_atleast_in_one_strings(test_strings))

print(f"\n3) characters that appear at least in two strings")
print(char_appear_atleast_in_two_strings(test_strings))

print(f"\n4) characters of alphabet, that were not used in any string")
print(char_not_used_strings(test_strings))
print("\n-----------------------------------------------------------------------------------")


# Task 4.10 Implement a function that takes a number N as an argument and returns a dictionary, where the key is a n
# (n ∈ [1, N]) and the value is the square of n (n**2). print(generate_squares(5)) >>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def generate_squares(input_value):
    d = dict()
    for x in range(1, input_value + 1):
        d[x] = x ** 2
    return d


print(f"Task 4.10: Implement a function that takes a number N as an argument and returns a dictionary, where the key "
      f"is a n (n ∈ [1, N]) and the value is the square of n (n**2).")
print(generate_squares(5))
print("\n-----------------------------------------------------------------------------------")


# Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers) and
# combines them into one dictionary. Dict values ​​should be summarized in case of identical keys def combine_dicts(
# *args): dict_1 = {'a': 100, 'b': 200} dict_2 = {'a': 200, 'c': 300} dict_3 = {'a': 300, 'd': 100} print(
# combine_dicts(dict_1, dict_2) >>> {'a': 300, 'b': 200, 'c': 300} print(combine_dicts(dict_1, dict_2, dict_3) >>> {
# 'a': 600, 'b': 200, 'c': 300, 'd': 100}

def combine_dicts(dict_1, dict_2, dict_3):
    return {**dict_1, **dict_2, **dict_3}

print(f"Task 4.11: Implement a function, that receives changeable number of dictionaries (keys - letters, "
      f"values - numbers) and combines them into one dictionary. Dict values should be summarized in case of "
      f"identical keys")
dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}
print(f"Input Values {dict_1}, {dict_2}, {dict_3} ")
print(f"Output Values ", combine_dicts(dict_1, dict_2, dict_3))


print("\n-----------------------------------------------------------------------------------")
