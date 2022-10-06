G = 10


def make_closure(string):
    def create_gen(string):
        while True:
            for i in string:
                yield (i)
    generetor =create_gen(string)
    def inner():
        return next(generetor)
    return inner

f = make_closure('123R')
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())
