month = input("Введите название месяца: ").lower()
if month in ['январь', 'марта', 'май', 'июль', 'август', 'октябрь', 'декбрь']:
    print("В этом месяце 31 день.")
elif month in ['апрель', 'июнь', 'сентябрь', 'ноябрь']:
    print("В этом месяце 30 дней.")
elif month == 'февраль':
    print("Февраль может состоять из 28 или 29 дней.")
else:
    print("Неправильное название месяца.")
