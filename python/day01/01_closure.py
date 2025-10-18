def func_out():
    num1 = 10

    def func_inner(num2):
        result = num1 + num2
        print("result is:", result)

    return func_inner

new_func = func_out()

new_func(20)
new_func(10)

def config_name(name):

    def inner(msg):
        print(name + " : " + msg)

    return inner

tom = config_name("tom")

jerry = config_name("jerry")

tom("play with me! jexhsu!")
jerry("all right!")

def func_1():
    number_1 = 10

    def func_2():
        # modify outter func variables (use nonlocal)
        nonlocal number_1
        number_1 = 1000
        result = number_1 + 10
        print(result)

    return func_2

func_3 = func_1()
func_3()
