class MyDecorator(object):
    def __init__(self, func):
        self.__func = func

    def __call__(self):
        print("yes!")
        self.__func()

@MyDecorator
def show():
    print("waiting for u!")

show()

def mytest():
    print("xixi")

print(dir(mytest))
