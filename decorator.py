def outer(func):
    print("outer func")
    def inner(*args):
        print(" inner func")
        res=func(*args)
    return inner
@outer
def normal(name,age):
    print("normal func {},{}".format(name,age))
normal('abc',123)
