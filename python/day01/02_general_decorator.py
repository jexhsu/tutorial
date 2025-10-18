from time import time

print("-------------------------------")
def simple_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")


say_hello() # simple_decorator(say_hello)()

print("-------------------------------")
def runtime(func):
    def wrapper():
        startTime = time()
        func()
        endTime = time()
        print("runtime is :", endTime - startTime)
    return wrapper

@runtime
def loop():
    for i in range(10):
        print("i is: ", i)

loop()

print("-------------------------------")
def comment(func):
    def wrapper(num1, num2):
        print("caculating ......")
        func(num1, num2)
    return wrapper

@comment
def add_num(num1, num2):
    res = num1 + num2
    print("res is :", res)

add_num(1, 2)

print("-------------------------------")
def comment_return(func):
    def wrapper(num1, num2):
        print("caculating ......")
        res = func(num1, num2)
        return res
    return wrapper

@comment_return
def add_num_return(num1, num2):
    res = num1 + num2
    return res

res = add_num_return(1, 2)
print("res is :", res)

print("-------------------------------")
# args: arguments (tuples)
# kwargs: keyword arguments (dict)
def comment_args(func):
    def wrapper(*args, **kwargs):
        print("caculating ......")
        return func(*args, **kwargs)
    return wrapper

@comment_args
def add_num_args(*args, **kwargs):
    result = 0
    for val in args:
        result += val
    for val in kwargs.values():
        result += val
    return result

res = add_num_args(1, 2, 3, 4, a=5)
print("res is :", res)
