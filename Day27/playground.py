def add(*args):  # pass all numbahs
    sum = 0
    for element in args:
        sum += element
    return sum


print(add(2, 3, 5, 4))


def calc(n, **kwargs):  # each keyword is a dictionary
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n *= kwargs["add"]
    n *= kwargs["mult"]
    print(n)


calc(7, add=5, mult=4)
