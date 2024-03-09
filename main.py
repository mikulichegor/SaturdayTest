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
        pass
    elif answer == 'корень':
        good()
    elif answer == 'sin':
        pass
    elif answer == 'cos':
        pass
    elif answer == 'tg':
        pass

def good():

    import math

    num = float(input("Введите число: "))
    sqrt_num = math.sqrt(num)

    print("Корень числа", num, "равен", sqrt_num)


menu()