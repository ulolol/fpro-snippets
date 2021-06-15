try:
    a = 20
    b = 0
    print(a/b)
except ZeroDivisionError:
    print('divide by zero error')
finally:
    print('this will print anyways')

