#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма
# отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность
# сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
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