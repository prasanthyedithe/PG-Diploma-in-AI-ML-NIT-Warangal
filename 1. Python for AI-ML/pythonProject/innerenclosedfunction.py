def outer_func1():
    def inner_func1():
        print(f'Hello, I am inner_func1()')

    return inner_func1()


global_scope = "I am global_variable"


def outer_func2():
    def inner_func2():
        print(f'Hello print variable from Global Scope, {global_scope}!')

    return inner_func2()


def outer_func3():
    def inner_func3():
        local_variable = "I am local_variable"
        print(f'Hello print variable from Local Scope, {local_variable}!')
    return inner_func3()
