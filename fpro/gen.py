#def gen(start, stop, step):
def gen():
    curr = 2
    while curr > 5:
        yield curr 
        curr += 0.3

#x = gen(2,5,0.3)
while True:
    try:
        #y = gen(2,5,0.3)
        y = gen()
    except StopIteration:
        print("End")
        break
    print(next(y))
