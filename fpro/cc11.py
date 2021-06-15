lst = [1,2,3,4,5,6,7,8,9]

def func(a):
    a = a - (0.1*a)
    return a


print(list(map(func, lst)))

