def menu():

    answer = input('Выберите действие:\n+ - сложение\n- - вычитание\n* - умножение\n'
                   '/ - деление\n** - возведение в степень\n% - остаток от деления\n корень - корень\n'
                   'sin - синус\ncos - косинус\ntg - тангенс')
    if answer == '+':
        pass
    elif answer == '-':
        minus()
    elif answer == '*':
        pass
    elif answer == '/':
        division()
    elif answer == '**':
        power()
    elif answer == '%':
        pass
    elif answer == 'корень':
        pass
    elif answer == 'sin':
        pass
    elif answer == 'cos':
        pass
    elif answer == 'tg':
        pass


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