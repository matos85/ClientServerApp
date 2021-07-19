"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов не используя (методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

list_str_format = ['class', 'function', 'method']
list_for_byte_format = []
for i in list_str_format:
    res = bytes(i, 'utf-8')
    list_for_byte_format.append(res)

print('------------------------------------')
print(f'Исходный список: {list_str_format}')
print(f'Преобразованный список: {list_for_byte_format}')
for i in range(len(list_str_format)):
    print('------------------------------------')
    print(f'Сравним {i + 1}ое слово в списках:')
    print(f'Типы данных у слова: {list_str_format[i]} - в исходном списке: {type(list_str_format[i])},'
          f' в списке после преобразованиея {type(list_for_byte_format[i])}')
    print(f'Тип одинаковый? Ответ: {type(list_str_format[i]) == type(list_for_byte_format[i])}')
    print(f'Длина у слова: {list_str_format[i]} - в исходном списке: {len(list_str_format[i])},'
          f' в списке после преобразованиея {len(list_for_byte_format[i])}')
    print(f'Длина одинаковая? Ответ: {len(list_str_format[i]) == len(list_for_byte_format[i])}')
    print(f'Содержимое слова: {list_str_format[i]} - в исходном списке: {list_str_format[i]},'
          f' в списке после преобразованиея {list_for_byte_format[i]}')
    print(f'Содеражание одинаковое? Ответ: {list_str_format[i] == list_for_byte_format[i]}')
