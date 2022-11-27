import datetime

def gift_count (budget, month, birthdays):
    arr = {i for i in birthdays.items() if i[1].month == month}
    arr = sorted(arr, key=lambda x: x[1].day)
    arr = {i[0] + datetime.datetime.strftime(i[1], " (%d.%m.%Y)") for i in arr}
    arr = ', '.join(arr)
    print(f'Именинники в месяце {month}: {arr}. При бюджете {budget} они получат по {budget // len(arr)} рублей.')