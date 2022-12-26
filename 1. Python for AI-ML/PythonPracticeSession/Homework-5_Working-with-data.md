# Python Practice - Session 5


### Task 5.1
Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file called `sorted_names.txt`. Each name should start with a new line as in the following example:

```
Adele
Adrienne
...
Willodean
Xavier
```

### Task 5.2
Implement a function which search for most common words in the file.
Use `data/lorem_ipsum.txt` file as a example.

```python
def most_common_words(filepath, number_of_words=3):
    pass

print(most_common_words('lorem_ipsum.txt'))
>>> ['donec', 'etiam', 'aliquam']
```

> NOTE: Remember about dots, commas, capital letters etc.

### Task 5.3
File `data/students.csv` stores information about students in [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format.
This file contains the student’s names, age and average mark. 
1) Implement a function which receives file path and returns names of top performer students
```python
def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))
>>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
```

2) Implement a function which receives the file path with students info and writes CSV student information to the new file in descending order of age. 
Result:
``` 
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
```

### Task 5.4
Look through file `modules/legb.py`.

1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.

2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.

2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.

### Task 5.5
Implement a decorator `remember_result` which remembers last result of function it decorates and prints it before next call.

```python
@remember_result
def sum_list(*args):
	result = ""
	for item in args:
		result += item
	print(f"Current result = '{result}'")
	return result

sum_list("a", "b")
>>> "Last result = 'None'"
>>> "Current result = 'ab'"
sum_list("abc", "cde")
>>> "Last result = 'ab'" 
>>> "Current result = 'abccde'"
sum_list(3, 4, 5)
>>> "Last result = 'abccde'" 
>>> "Current result = '12'"
```

### Task 5.6
Implement a decorator `call_once` which runs a function or method once and caches the result.
All consecutive calls to this function should return cached result no matter the arguments.

```python
@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))
>>> 55
print(sum_of_numbers(999, 100))
>>> 55
print(sum_of_numbers(134, 412))
>>> 55
print(sum_of_numbers(856, 232))
>>> 55
```


### Task 5.7*
Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.
Try to change x to a list `[1,2,3]`. Explain the result.
Try to change import to `from x import *` where x - module names. Explain the result. 


### Materials
* [Decorators](https://realpython.com/primer-on-python-decorators/)
* [Decorators in python](https://www.geeksforgeeks.org/decorators-in-python/)
* [Python imports](https://pythonworld.ru/osnovy/rabota-s-modulyami-sozdanie-podklyuchenie-instrukciyami-import-i-from.html)
* [Files in python](https://realpython.com/read-write-files-python/)
