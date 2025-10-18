print("-------------------------------")
def make_p(func):
    def wrapper():
        res = "<p>" + func() + "<p>"
        return res
    return wrapper

def make_div(func):
    def wrapper():
        res = "<div>" + func() + "<div>"
        return res
    return wrapper

@make_div
@make_p
def content():
    return "Hello! python!"

res = content()
# res = make_div(make_p(content))()
print(res)
