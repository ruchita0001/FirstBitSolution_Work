print('--- Simple Calculator ---')

try:
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    op = input('Enter operator (+, -, *, /): ')

    # Operator check
    if op not in ['+', '-', '*', '/']:
        raise Exception('Invalid Operator')

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2   # may raise ZeroDivisionError

except ValueError:
    print('Error: Invalid Number entered')

except ZeroDivisionError:
    print('Error: Division by zero is not allowed')

except Exception as e:
    print('Error:', e)

else:
    print('Result:', result)

finally:
    print('--- Program End ---')
