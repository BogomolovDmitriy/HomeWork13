# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов

import os

path = os.path.abspath("Exercise5") # определяем адрес папки с файлами

def readFile(str):
    data = open(str, "r")
    line = data.readline()
    data.close()
    return line

my_str1 = readFile(path + "/text1.txt") # создаем список многочлена из первого файла
my_str2 = readFile(path + "/text2.txt") # создаем список многочлена из второго файла

def dict(string):
    str = string[:len(string) - 2] # удаляем из списка последние два символа "=0"
    str = str.split("x") # создаем список, где разделителем является "х"

    str[0] = str[0] + str[1][:1]
    for i in range(1, len(str) - 1):
        str[i] = str[i][1:] + str[i + 1][: 1]
    str[-1] = str[-1][1:]
    str.pop()
    dict = {num[-1]: (num[: -1]) for num in str} # создаем словарь, где ключем служит степень
    return dict

my_dict1 = dict(my_str1)
my_dict2 = dict(my_str2)

# создаем новый словарь, где приводим "подобные" по ключам из первого и второго словаря
aux_dict = {}
for item in my_dict2.keys():
    aux_dict[item] = int(my_dict1[item]) + int(my_dict2[item])

# итоговый многочлен после сложение исходных
polynomial = ""
for i in aux_dict.keys():
    polynomial += str(aux_dict[i]) + "x" + str(list(aux_dict.keys())[list(aux_dict.values()).index(aux_dict[i])])
polynomial += "=0"

print(polynomial)

# записываем получившийся результат в файл
data = open(path + "/text3.txt", "w")
data.writelines(polynomial)
data.close()

