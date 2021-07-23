"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet


def mani_ping(ping_list):
    YA_PING = subprocess.Popen(ping_list, stdout=subprocess.PIPE)
    for line in YA_PING.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'), end='')


ARGS = ['youtube.com', 'yandex.ru']
for addsource in ARGS:
    ping_list = []
    ping_list.append('ping')
    ping_list.append(addsource)
    print(f'Пингую сайт:{addsource}')
    mani_ping(ping_list)
    print('-----------------------------')
