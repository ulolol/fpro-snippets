
def div(a,b):
    res = a/b
    return res


x = int(input('enter no. 1'))
y = int(input('enter no. 2'))

try:
    R = div(x,y)
    print(R)
except ZeroDivisionError:
    print('Divide by zero error. No. 2 CANNOT be 0 you dummy !')
finally:
    print('you better not be a dumbo!')
