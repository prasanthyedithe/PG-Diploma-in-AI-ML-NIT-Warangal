# Python Practice - Session 6

from collections import OrderedDict
import string

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("\nPython Practice - Session 6")
print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

# Task 6.1
# Implement a Counter class which optionally accepts the start value and the counter stop value.
# If the start value is not specified the counter should begin with 0.
# If the stop value is not specified it should be counting up infinitely.
# If the counter reaches the stop value, print "Maximal value is reached."
# Implement to methods: "increment" and "get"

global_start = 0
global_stop = 0


def counter_with_noargs():
    global global_stop
    global_stop = 0


def counter_with_start(start):
    global global_start
    global_start = start


def counter_with_start_stop(start, stop):
    global global_start, global_stop
    global_start = start
    global_stop = stop


def increment():
    global global_start, global_stop

    if global_start == 0 & global_stop == 0:
        global_start = 0
        global_stop = 1
    elif global_start >= 0 & global_stop == 0:
        if global_start != global_stop:
            global_stop = global_start + 1
            global_start = global_stop
        else:
            print("Maximal value is reached.")
    elif global_start >= 0 & global_stop >= 0:
        if global_start != global_stop:
            global_stop = global_start + 1
            global_start = global_stop
        else:
            print("Maximal value is reached.")


def get():
    print("get():stop", global_stop)


counter_with_start(start=42)
increment()
get()

global_start = 0
global_stop = 0

counter_with_noargs()
increment()
get()

counter_with_start_stop(start=42, stop=43)
increment()
get()
increment()
get()

print("\n-----------------------------------------------------------------------------------")


# Task 6.2
# Implement custom dictionary that will memorize 10 latest changed keys.
# Using method "get_history" return this keys.

def get_history():
    res = OrderedDict(reversed(list(user_ordered_dict.items())))
    for x in list(res)[0:10]:
        print(x)


print("\nThis is an Ordered Dict:\n")
user_ordered_dict = OrderedDict([('Jake', '10'), ('John', '20'), ('Ross', '40'), ('Joke', '10'), ('Test', '20'),
                                 ('Hello', '40'), ('Fake', '10'), ('Bake', '20'), ('Roop', '40'),
                                 ('Jhonny', '10'), ('Browny', '20'), ('Growny', '40')])
print("Actual Items \n")
print(user_ordered_dict)

user_ordered_dict['Jake'] = '110'
user_ordered_dict.move_to_end('Jake', last=True)

user_ordered_dict['Ross'] = '210'
user_ordered_dict.move_to_end('Ross', last=True)

user_ordered_dict['Browny'] = '410'
user_ordered_dict.move_to_end('Browny', last=True)

user_ordered_dict['Fake'] = '420'
user_ordered_dict.move_to_end('Fake', last=True)

get_history()

print("\n-----------------------------------------------------------------------------------")
# Task 6.3
# Implement The Keyword encoding and decoding for latin alphabet.
all_alphabets = list(string.ascii_uppercase)
keyword = "crypto"


def encode_text(message):
    keyword1 = keyword.upper()

    # converts message to list
    msg = []
    for i in message:
        msg.append(i.upper())

    # removes default elements

    def duplicates(list):
        key = []
        for i in list:
            if i not in key:
                key.append(i)

        return key

    keyword1 = duplicates(keyword1)

    # Stores the encryption list
    encrypting = duplicates(keyword1 + all_alphabets)

    # removes spaces from the encryption list
    for i in encrypting:
        if i == ' ':
            encrypting.remove(' ')

    ciphertext = ""

    # maps each element of the message to the encryption list and stores it in ciphertext
    for i in range(len(msg)):
        if msg[i] != ' ':
            ciphertext = ciphertext + encrypting[all_alphabets.index(msg[i])]
        else:
            ciphertext = ciphertext + ' '

    print("Keyword : ", keyword)
    print("Message before Ciphering : ", message)
    print("Ciphered Text : ", ciphertext)


def decode_text(ciphertext):
    keyword2 = keyword.upper()

    # converts message to list
    ct = []
    for i in ciphertext:
        ct.append(i.upper())

    # removes default elements

    def duplicates(list):
        key = []
        for i in list:
            if i not in key:
                key.append(i)

        return key

    keyword2 = duplicates(keyword2)

    # Stores the encryption list
    encrypting = duplicates(keyword2 + all_alphabets)

    # removes spaces from the encryption list
    for i in encrypting:
        if i == ' ':
            encrypting.remove(' ')

    # maps each element of the message to the encryption list and stores it in ciphertext
    message = ""
    for i in range(len(ct)):
        if ct[i] != ' ':
            message = message + all_alphabets[encrypting.index(ct[i])]
        else:
            message = message + ' '

    print("Keyword : ", keyword)
    print("Ciphered Text : ", ciphertext)
    print("Message before Ciphering : ", message)


encode_text("Hello world")
decode_text("BTGGJ VJMGP")

print("\n-----------------------------------------------------------------------------------")


# Task 6.4
# Create hierarchy out of birds.

class Bird:

    def __init__(self, name):
        self.name = name

    def fly(self):
        print("Flying")

    def walk(self):
        print(self.name, "bird can walk")


class FlyingBird:

    def __init__(self, name, ration="1"):
        self.name = name
        self.ration = ration

    def fly(self):
        print("Flying")

    def walk(self):
        print("Walking")


class NonFlyingBird:

    def __init__(self, name, ration="1"):
        self.name = name
        self.ration = ration

    def eat(self):
        print("It eats mostly fish")

    def walk(self):
        print("Walking")

    def swim(self):
        print(self.name," bird can swim")


class SuperBird:

    def __init__(self, name, ration="1"):
        self.name = name
        self.ration = ration

    def fly(self):
        print("Flying")

    def eat(self):
        print("Eat")

    def walk(self):
        print("Walking")

    def swim(self):
        print("Swim")


b= Bird("Any")
b.walk()

p1 = NonFlyingBird("Penguin", "fish")
p1.swim()
# p1.fly()
p1.eat()