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
