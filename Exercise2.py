# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите число: "))

temp_list = []
for i in range(n + 1):
    temp_list.append(i)

temp_list[1] = 0
i = 2
while i <= n / 2:
    if temp_list[i] != 0 :
        j = i + i
        while j <= n:
            temp_list[j] = 0
            j = j + i
    i += 1

prime_list = []
for i in temp_list:
    if i != 0:
        prime_list.append(i)

num_list = []
b = n
while b != 1:
    for j in prime_list:
        if b % j == 0:
            num_list.append(j)
            b /= j
            break
      
print(f"Список простых множителей числа {n}: {num_list}")
    