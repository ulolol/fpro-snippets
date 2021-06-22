import time
#def gen(start, stop, step):
def gen():
    curr = 2
    while curr > 5:
        yield curr 
        curr += 0.3


y = gen()
print(type(y))
print(y.__next__())
#x = gen(2,5,0.3)
while True:
    try:
        #y = gen(2,5,0.3)
        
        for i in y:
            print(i)
            time.sleep(0.5)
    except StopIteration:
        print("End")
        break
    
