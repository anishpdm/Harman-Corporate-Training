

def calculator(func):
    print("Execute this First")
    def inner(a, b):
        print(a)
        print(b)
        return func(a,b)
    return inner


@calculator  # Execute this First
def add(a,b):
    print(a+b)

add(10,20)




# hello(printname)


