time_sec = int(input('Введите время в секундах: '))
minutes = int(time_sec / 60)
print(f'{time_sec} секунд в формате чч:мм:сс будет: {(minutes // 60):02}:{(minutes % 60):02}:{(time_sec % 60):02}')