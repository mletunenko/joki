from collections import defaultdict


# Итерируемся по позициям символов в строке, подсчитывая число одинаковых символов. Все операции производятся
# со строками, приведенными к нижнему регистру, что бы регистр не влиял на уникальность. Функция вернет первый
# уникальный символ в нужном регистре, поскольку итерация происходит по позиции в строке, а не по символам.

def first_non_repeating_letter(string):
    for i in range(len(string)):
        l_string = string.lower()
        if l_string.count(l_string[i]) == 1:
            return string[i]
    return ''


# Потребуется еще одна функция create_gen, в которой будет создаваться бесконечный генератор из переданной
# строки. Функцию wrapper применим, что бы обернуть функцию next(). Поскольку переменная generator для функции wrapper
# является внешней, состояние генератора будет сохранено.

def create_gen(string):
    while True:
        for i in string:
            yield (i)


def make_looper(string):
    generator = create_gen(string)

    def wrapper():
        return next(generator)

    return wrapper


# С помощью рекурсии перебираем все уникальные комбинации номиналов и подсчитываем в переменной n те комбинации,
# которые удовлетворяют условию. В условии задачи сказано, что функция должна принимать на вход две переменные,
# в данном варианте решения три переменные, но поскольку при первом вызове функции n всегда = 0, то мы вправе
# указать n по умолчанию = 0 и передавать только 2 аргумента. Иначе, необходимо создать вложенную функцию и передать
# ей n третьим аргументом

def count_change(sum, denoms, n=0):
    for i in range(len(denoms)):
        if sum - denoms[i] > 0:
            n = count_change(sum - denoms[i], denoms[i:], n)
        elif sum - denoms[i] == 0:
            n += 1
    return n


# Выполним две проверки (на "состав" слова и на порядок символов):
# 1) Проверим что строку s можно составить из строк part1 и part1 сравнив словари, возвращаемые функцией create_counter
# 2) Проверим что порядок символов в частичке не противоречит порядку в главной строке с помощью функции check_order
# 3) Все проверки выполним в функции is_merge

def create_counter(s):
    dict = defaultdict(int)
    for i in s:
        dict[i] += 1
    return dict


def check_order(s, part):
    for i in part:
        pos = s.find(i)
        if pos >= 0:
            s = s[pos:]
            continue
        else:
            return False
    return True


def is_merge(s, part1, part2):
    if create_counter(s) == create_counter(part1 + part2) and check_order(s, part1) and check_order(s, part2):
        return True
    return False
