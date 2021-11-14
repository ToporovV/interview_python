# Разработать генератор случайных чисел. В функцию передавать начальное и
# конечное число генерации (нуль необходимо исключить). Заполнить этими данными
# список и словарь. Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
# Вывести содержимое созданных списка и словаря.

from random import randint


def generator(min_, max_):
    if min_ == 0 or max_ <= min_:
        return print('Минимальное число не должно равняться 0, минимум должен быть меньше максимума.')
    rand_list = [randint(min_, max_) for _ in range(10)]
    rand_dict = {f"elem_{i + 1}": rand_list[i] for i in range(len(rand_list))}
    print(rand_list, rand_dict)


generator(2, 1)
generator(0, 1)
generator(1, 10)