def first_non_repeating_letter(string):
    for i in range(len(string)):
        l_string = string.lower()
        if l_string.count(l_string[i]) == 1:
            return string[i]
    return ''

def make_looper(string):
    def create_func(string):
        def create_gen(string):
            while True:
                for i in string:
                    yield (i)
        gen = create_gen(string)
        return next(gen)
    return create_func(string)


print(a = make_looper('aass'))