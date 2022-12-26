# Python Practice - Session 7


### Task 7.1
Implement class-based context manager for opening and working with file, including handling exceptions. Do not use 'with open()'. Pass filename and mode via constructor.

### Task 7.2
Implement context manager for opening and working with file, including handling exceptions with @contextmanager decorator.

### Task 7.3
Implement decorator with context manager support for writing execution time to log-file. See contextlib module.

### Task 7.4
Implement decorator for supressing exceptions. If exception not occure write log to console.

### Task 7.5
Implement a function to check that number is even (number > 3). A number should be passed as a string. Throw different exceptions for different situations. Custom exceptions must be derived from custom base exception (not Base Exception class).

### Task 7.6
Create console program for proving Goldbach's conjecture. Program accepts number for input and print result. For pressing 'q' program succesfully close. Use function from Task 7.5 for validating input, handle all exceptions and print user friendly output.

### Task 7.7
Implement your custom collection called MyNumberCollection. It should be able to contain only numbers. It should NOT inherit any other collections.
If user tries to add a string or any non numerical object there, exception `TypeError` should be raised. Method init sholud be able to take either 
`start,end,step` arguments, where `start` - first number of collection, `end` - last number of collection or some ordered iterable 
collection (see the example).
Implement following functionality:
* appending new element to the end of collection
* concatenating collections together using `+`
* when element is addressed by index(using `[]`), user should get square of the addressed element.
* when iterated using cycle `for`, elements should be given normally
* user should be able to print whole collection as if it was list.
Example:
```python
col1 = MyNumberCollection(0, 5, 2)
print(col1)
>>> [0, 2, 4, 5]
col2 = MyNumberCollection((1,2,3,4,5,))
print(col2)
>>> [1, 2, 3, 4, 5]
col3 = MyNumberCollection((1,2,3,"4",5))
>>> TypeError: MyNumberCollection supports only numbers!
col1.append(7)
print(col1)
>>> [0, 2, 4, 5, 7]
col2.append("string")
>>> TypeError: 'string' - object is not a number!
print(col1 + col2)
>>> [0, 2, 4, 5, 7, 1, 2, 3, 4, 5]
print(col1)
>>> [0, 2, 4, 5, 7]
print(col2)
>>> [1, 2, 3, 4, 5]
print(col2[4])
>>> 25
for item in col1:
    print(item)
>>> 0 2 4 5 7
```

### Task 7.8
Implement your custom iterator class called MySquareIterator which gives squares of elements of collection it iterates through.
Example:
```python
lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
for item in itr:
    print(item)
>>> 1 4 9 16 25

```

### Task 7.9
Implement an iterator class EvenRange, which accepts start and end of the interval as an init arguments and gives only even numbers during iteration.
If user tries to iterate after it gave all possible numbers `Out of numbers!` should be printed.  
_Note: Do not use function `range()` at all_
Example:
```python
er1 = EvenRange(7,11)
next(er1)
>>> 8
next(er1)
>>> 10
next(er1)
>>> "Out of numbers!"
next(er1)
>>> "Out of numbers!"
er2 = EvenRange(3, 14)
for number in er2:
    print(number)
>>> 4 6 8 10 12 "Out of numbers!"
```

### Task 7.10
Implement a generator which will generate odd numbers endlessly.
Example:
```python
gen = endless_generator()
while True:
    print(next(gen))
>>> 1 3 5 7 ... 128736187263 128736187265 ...
```

### Task 7.11
Implement a generator which will geterate [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number) endlessly.
Example:
```python
gen = endless_fib_generator()
while True:
    print(next(gen))
>>> 1 1 2 3 5 8 13 ...
```


### Materials
* [Exceptions](https://realpython.com/python-exceptions/)
* [Contextlib](https://python-scripts.com/contextlib)
* [Context Managers](https://book.pythontips.com/en/latest/context_managers.html)
* [Python iterator](https://www.programiz.com/python-programming/iterator)
* [Iterators](https://anandology.com/python-practice-book/iterators.html)
* [Iterators and Generators](https://www.youtube.com/watch?v=jTYiNjvnHZY)
* [List comprehension and generator expressions](https://www.youtube.com/watch?v=3dt4OGnU5sM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=20)

