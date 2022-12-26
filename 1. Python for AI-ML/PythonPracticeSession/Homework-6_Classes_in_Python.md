﻿﻿﻿﻿﻿﻿# Python Practice - Session 4


### Task 6.1
Implement a Counter class which optionally accepts the start value and the counter stop value.
If the start value is not specified the counter should begin with 0.
If the stop value is not specified it should be counting up infinitely.
If the counter reaches the stop value, print "Maximal value is reached."

Implement to methods: "increment" and "get"

* <em>If you are familiar with Exception rising use it to display the "Maximal value is reached." message.</em>

Example:
```python
>>> c = Counter(start=42)
>>> c.increment()
>>> c.get()
43

>>> c = Counter()
>>> c.increment()
>>> c.get()
1
>>> c.increment()
>>> c.get()
2

>>> c = Counter(start=42, stop=43)
>>> c.increment()
>>> c.get()
43
>>> c.increment()
Maximal value is reached.
>>> c.get()
43
```

#### Task 6.2
Implement custom dictionary that will memorize 10 latest changed keys.
Using method "get_history" return this keys.


Example:
```python
>>> d = HistoryDict({"foo": 42})
>>> d.set_value("bar", 43)
>>> d.set_value("foo", 1)
>>> d.get_history()

["bar", "foo"]
```

<em>After your own implementation of the class have a look at collections.deque https://docs.python.org/3/library/collections.html#collections.deque </em>


### Task 6.3
Implement The Keyword encoding and decoding for latin alphabet.
The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
Add the provided keyword at the begining of the alphabet.
A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet. 
Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.

<em> Encryption:
Keyword is "Crypto"

* A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
* C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
</em>

Example:
```python
>>> cipher = Cipher("crypto")
>>> cipher.encode("Hello world")
"Btggj vjmgp"

>>> cipher.decode("Fjedhc dn atidsn")
"Kojima is genius"
```

### Task 6.4
Create hierarchy out of birds. 
Implement 4 classes:
* class `Bird` with an attribute `name` and methods `fly` and `walk`.
* class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value. 
Implement the method `eat` which will describe its typical ration.
* class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
Add same "eat" method but with other implementation regarding the swimming bird tastes.
* class `SuperBird` which can do all of it: walk, fly, swim and eat.
But be careful which "eat" method you inherit.

Implement str() function call for each class.

Example:
```python
>>> b = Bird("Any")
>>> b.walk()
"Any bird can walk"

p = NonFlyingBird("Penguin", "fish")
>> p.swim()
"Penguin bird can swim"
>>> p.fly()
AttributeError: 'Penguin' object has no attribute 'fly'
>>> p.eat()
"It eats mostly fish"

c = FlyingBird("Canary")
>>> str(c)
"Canary can walk and fly"
>>> c.eat()
"It eats mostly grains"

s = SuperBird("Gull")
>>> str(s)
"Gull bird can walk, swim and fly"
>>> s.eat()
"It eats fish"
```

Have a look at __mro__ method of your last class.

### Task 6.5

A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance. 
Implement singleton logic inside your custom class using a method to initialize class instance.

Example:

```python
>>> p = Sun()
>>> f = Sun()
>>> p is f
True
```

### Task 6.6 
Implement a class Money to represent value and currency.
You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication, addition and subtraction).
Tip: use class attribute exchange rate which is dictionary and stores information about exchange rates to your default currency:
```python
exchange_rate = {
    "EUR": 0.93,
    "BYN": 2.1,
    "JOY": 130.84,
    ...
}
```

Example:
```python
x = Money(10, "BYN")
y = Money(11) # define your own default value, e.g. “USD”
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8) # result in “EUR”
>>34.29 EUR

lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)
print(s) #result in “BYN”
>>33.29 BYN
```

<em>Have a look at @functools.total_ordering</em>

### Task 6.7

Implement a Pagination class helpful to arrange text on pages and list content on given page. 
The class should take in a text and a positive integer which indicate how many symbols will be allowed per each page (take spaces into account as well).
You need to be able to get the amount of whole symbols in text, get a number of pages that came out and method that accepts the page number and return quantity of symbols on this page.
If the provided number of the page is missing print the warning message "Invalid index. Page is missing". If you're familliar with using of Excpetions in Python display the error message in this way.
Pages indexing starts with 0.

Example:
```python
>>> pages = Pagination('Your beautiful text', 5)
>>> pages.page_count
4
>>> pages.item_count
19

>>> pages.count_items_on_page(0)
5
>>> pages.count_items_on_page(3)
4
>>> pages.count_items_on_page(4)
Exception: Invalid index. Page is missing.
```
Optional: implement searching/filtering pages by symblos/words and displaying pages with all the symbols on it.
If you're querying by symbol that appears on many pages or if you are querying by the word that is splitted in two return an array of all the occurences.

Example:
```python
>>> pages.find_page('Your')
[0]
>>> pages.find_page('e')
[1, 3]
>>> pages.find_page('beautiful')
[1, 2]
>>> pages.find_page('great')
Exception: 'great' is missing on the pages
>>> pages.display_page(0)
'Your '
```


### Materials
* [Classes](https://docs.python.org/3/tutorial/classes.html)
* [OOP in python](https://realpython.com/python3-object-oriented-programming/)
* [Python OOP](https://proglib.io/p/python-oop/)
* [Magic methods](https://habr.com/ru/post/186608/)
* [Method resolution order](https://medium.com/technology-nineleaps/python-method-resolution-order-4fd41d2fcc)
* [Classm & Static methods](https://realpython.com/instance-class-and-static-methods-demystified/)

