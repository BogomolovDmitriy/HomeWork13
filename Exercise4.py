# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input("Введите число: "))
str = ""
for i in range(k + 1):
    str += f"{randint(0, 100)} * x ** {i} + " 
print(f"0 = {str[0: len(str) - 2]}")
