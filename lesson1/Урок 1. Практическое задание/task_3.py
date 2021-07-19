"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""

words = ['attribute', 'класс', 'функция', 'type']

# for i in list_str_format:
#     res = bytes(i, 'utf-8')
#     list_for_byte_format.append(res)


for line in words:
    res = bytes(line, 'utf-8')
    print(line)
    print(res)
