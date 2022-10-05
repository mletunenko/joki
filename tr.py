def func(string):
    for i in string:
        yield i


print(type(func('sdsd')))