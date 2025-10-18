def func_out():
    num1 = 10

    def func_inner(num2):
        result = num1 + num2

        print("result is:", result)

    return func_inner


new_func = func_out()

new_func(20)
new_func(10)
