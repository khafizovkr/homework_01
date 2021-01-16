a = 5
b = 7
day = 1
while b > a:
    print(f'{day}-й день: {round(a, 2)}')
    a = a * 1.1
    day += 1
print(f'{day}-й день: {round(a, 2)}')
print(f'на {day}-й день спортсмен достиг результата - не менее {b} км')