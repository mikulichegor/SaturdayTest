import math
def menu():
    answer = input('Выберите действие:\n+ - сложение\n- - вычитание\n* - умножение\n'
                   '/ - деление\n** - возведение в степень\n% - остаток от деления\n корень - корень\n'
                   'sin - синус\ncos - косинус\ntg - тангенс')
    if answer == '+':
        func()
    elif answer == '-':
        minus()
    elif answer == '*':
        pass
    elif answer == '/':
        division()
    elif answer == '**':
        power()
    elif answer == '%':
        bebra1488()
    elif answer == 'корень':
        good()
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



def func():
    o = int(input('Введите первое число: '))
    u = int(input('Введите второе число: '))
    print(o + u)

def good():

    import math

    num = float(input("Введите число: "))
    sqrt_num = math.sqrt(num)

    print("Корень числа", num, "равен", sqrt_num)



def minus():
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    min = a - b
    print(min)



def division():
    x=input('Введите первое число:')
    y=input('Введите второе число:')
    div=x/y
    print(f'Div:{div}')


def power():
    n = int(input("Введите число "))
    p = int(input("Введите степень для числа "))
    result = n**p
    print("Ответ: ", result)



menu()
