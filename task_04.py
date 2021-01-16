#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и
# арифметические операции.
number = int(input('Введите целое положительное число: '))
max = 0
while number >= 1:
    number_to_compare = number % 10
    number = number // 10
    if number_to_compare > max:
        max = number_to_compare
print(max)