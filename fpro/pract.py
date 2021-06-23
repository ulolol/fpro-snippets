l = int(input("enter the size : "))
num = list()
for n in range(0,l):
    num.append(int(input("enter the number : ")))

avg = sum(num)/l
print(avg)

num = input("enter the number : ")
rev = num[::-1]
print(rev)

num = int(input("enter the num : "))
sum = 0
while (num>0):
    n = num%10
    sum +=n
    num= num //10
print("sum = ", sum)