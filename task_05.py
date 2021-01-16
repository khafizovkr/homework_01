income = int(input('Выручка вашей компании: '))
expenses = int(input('Издержки вашей компании: '))
if income > expenses:
    print('Вы работаете на прибыль')
    rentab = (income - expenses) / income
    print(f'Рентабельность выручки: {round(rentab, 2)}')
    number_of_employees = int(input('Количество сотрудников в фирме: '))
    income_per_employee = (income - expenses) / number_of_employees
    print(f'Прибыль фирмы на сотрудника {income_per_employee}')
elif income == expenses:
    print('Выручка равна издержкам')
else:
    print('Вы работаете в убыток')