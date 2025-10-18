def return_comment(caculate):
    def comment(func):
        def wrapper(a, b):
            print(f"caculating {caculate} .......")
            func(a, b)
        return wrapper
    return comment

@return_comment(caculate="add")
def add_number(a, b):
    result = a + b
    print("result is :", result)

@return_comment(caculate="product")
def product_number(a, b):
    result = a * b
    print("result is :", result)

@return_comment(caculate="sub")
def sub_number(a, b):
    result = a - b
    print("result is :", result)

a = 10
b = 90
add_number(a, b)
product_number(a, b)
sub_number(a, b)
