#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input('Введите натуральное число: '))
i = 2
new_lst = []
orig_num = num
while i <= num:
    if num % i == 0:
        new_lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f'Простые множители числа {orig_num}: {new_lst}')