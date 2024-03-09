def menu():
    answer = input('Выберите действие:\n+ - сложение\n- - вычитание\n* - умножение\n'
                   '/ - деление\n** - возведение в степень\n% - остаток от деления\n корень - корень\n'
                   'sin - синус\ncos - косинус\ntg - тангенс')
    if answer == '+':
        pass
    elif answer == '-':
        pass
    elif answer == '*':
        pass
    elif answer == '/':
        pass
    elif answer == '**':
        pass
    elif answer == '%':
        bebra1488()
    elif answer == 'корень':
        pass
    elif answer == 'sin':
        pass
    elif answer == 'cos':
        pass
    elif answer == 'tg':
        pass
def bebra1488():
    number = float(input("Введите число: "))
    percent = float(input("Введите процент: "))

    result = number * (percent / 100)
    print(f"{percent}% от {number} равно {result}")


menu()
