import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Делить на ноль нельзя"

def power(a, b):
    return a ** b

def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Невозможно извлечь квадратный корень из отрицательного числа"

def factorial(a):
    if a >= 0:
        return math.factorial(a)
    else:
        return "Факториал определен только для неотрицательных целых чисел"

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def tan(a):
    return math.tan(a)

while True:
    try:
        operation = input("Выберите операцию (+, -, *, /, **, sqrt, !, sin, cos, tan): ")
        if operation not in ('+', '-', '*', '/', '**', 'sqrt', '!', 'sin', 'cos', 'tan'):
            raise ValueError

        if operation in ('+', '-', '*', '/', '**'):
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            else:
                result = power(num1, num2)

        elif operation == 'sqrt':
            num = float(input("Введите число: "))
            result = square_root(num)

        elif operation == '!':
            num = int(input("Введите число: "))
            result = factorial(num)

        else:
            num = float(input("Введите угол в радианах: "))
            if operation == 'sin':
                result = sin(num)
            elif operation == 'cos':
                result = cos(num)
            else:
                result = tan(num)

        print("Результат:", result)
        break

    except ValueError:
        print("Некорректный ввод. Попробуйте еще раз.")
    except Exception as e:
        print("Ошибка при выполнении операции:", e)
        