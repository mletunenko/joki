from time import time
# Итерируемся по позициям символов в строке, подсчитывая число одинаковых символов. Все операции производятся
# со строками, приведенными к нижнему регистру, что бы регистр не влиял на уникальность. Функция вернет первый
# уникальный символ в нужном регистре, поскольку итерация происходит по позиции в строке.
def first_non_repeating_letter(string):
    for i in range(len(string)):
        l_string = string.lower()
        if l_string.count(l_string[i]) == 1:
            return string[i]
    return ''

# Потребуется еще одна функция create_gen которая, в которой будет создаваться бесконечный генератор из переданной
# строки. Функцию wrapper применим, что бы обернуть функцию next(). Поскольку переменная generator для функции wrapper
# является внешней, состояние генератора будет сохранено.
def make_looper(string):
    def create_gen(string):
        while True:
            for i in string:
                yield (i)
    generator =create_gen(string)
    def wrapper():
        return next(generator)
    return wrapper

# С помощью рекурсии перебираем все уникальные комбинации номиналов и подсчитываем в переменной n те комбинации,
# которые удовлетворяют условию. В условии задачи сказано, что функция должна принимать на вход две переменные,
# в данном варианте решения три переменные, но поскольку при первом вызове функции n всегда = 0, то мы вправе
# указать n по умолчанию = 0 и передавать только 2 аргумента. Иначе, необходимо создать вложенную функцию и передать
# в ее аргумент n
def count_change(sum, denoms, n=0):
    for i in range(len(denoms)):
        if sum - denoms[i] > 0:
            n = count_change(sum - denoms[i], denoms[i:], n)
        elif sum - denoms[i] == 0:
            n += 1
    return n


g = make_looper('world')
print(g())
print(g())
print(g())
print(g())
print(g())
