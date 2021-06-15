def fun0(a):
    a = a - (0.1*a)
    return a


def fun1(b):
    b = b - (0.05*b)
    return b


x = 100
y = fun0(x)
z = fun1(y)

print(z)
