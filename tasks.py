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

def make_looper(string):
    def create_func():
        gen = iter(string)
        return
    return create_func()

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
