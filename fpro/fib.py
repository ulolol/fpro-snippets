def fib(num):
    if num <=1:
        return 1
    return fib(num-1) + fib(num-2)
print("0")
for x in range(10):
    print(fib(x))

a = ['a','b','c','d','e','f','g']
print(' '.join(a))
print(a)