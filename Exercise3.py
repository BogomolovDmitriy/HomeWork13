# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

a = [2, 3, 3, 5, 1, 6, 2]
b = []
for i in a:
    count = 0
    for j in range(len(a)):
        if a[j] == i:
            count += 1
    if count == 1:
        b.append(i)

print(b)