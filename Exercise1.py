# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

n = int(input("Введите число: "))

# # формула для вычисления числа ПИ
pi = 16 * math.atan(1 / 5) - 4 * math.atan(1 / 239)

print(f"{pi:.{n}f}")

