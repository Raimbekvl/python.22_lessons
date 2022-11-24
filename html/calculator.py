while True:
    try:
        a = int(input('Введите 1 число :'))
        b = int(input('Введите 2 число :'))
        c = input('Выберите операцию (/, +, -, *):')
        if c == '+':
            print(a+b)
        elif c == '-':
            print(a - b)
        elif c == '*':
            print(a * b)
        elif c == '/':
            print(a / b)
        else:
            print('Выберите правильную операцию !!!')
    except ZeroDivisionError:
        print('На ноль делить нельзя !')
    except ValueError:
        print('Вы вели не число !')  
    finally:
        z = input('Хотите продолжить ? yes/no :')
        if z.lower() == 'no' :
            break
    