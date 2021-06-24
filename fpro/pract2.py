 

a = int(input("enter a num : "))
sum = 0
b = a
while (b > 0):
    x = b%10
    sum = sum + x**3
    b = b//10
if sum == a:
    print("armstrong")
else:
    print("not armstrong")
 

 
n=int(input("Enter any number: "))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
    print("The number is an armstrong number. ")
else:
    print("The number isn't an arsmtrong number. ")
 





 

num = int(input("Enter a num : "))

def fact(num):
    facto = 1
    for i in range(1,num+1):
        facto = facto * i
        print("facto : ",facto)
    return facto

a = num 
sum = 0
while(a > 0):
    x = a%10
    print("x : ",x)
    sum = sum + fact(x)
    print(sum)
    a = a//10

if sum == num:
    print("strong")
else:
    print("not strong")

 

 
num = [43,5,56,56,67,23]

print(sorted(num)[-2])
 
 
lst = [23,233,423,2434,221,12]

a = lst[0]
b = lst[-1]
c = a 
a = b
b = c

lst[0] = a
lst[-1] = b

print(lst)

 

 
val = input("enter string ")

pal = val[::-1]

if pal == val:
    print("palindrome")
else:
    print("not palindrome")
 

 
sent = input("enter sentence : ")
avg = 0
c = 0
for word in sent.split():
    print(word)
    avg =avg + len(word)
    print(avg)
    c = c+ 1
    print(c)

print("avg : ",(avg/c))

 
 
n1 = input("enter num 1 +ve or -ve ")
n2 = input("enter num 2 +ve or -ve ")

print(eval(n1)+eval(n2))

 

 
import collections
val = input("enter the string :  ")
new = collections.Counter(val)

for i, x in enumerate(val):
    if new[x] == 1:
        print(i)
        exit()
print("-1")
 
 
s = "radkar"
for i in range(len(s)):
    t = s[:i] + s[i+1:]
    print(t)
    if t == t[::-1]:
        #print(t)
        print("palin")
    else:
        print("not")
 


 
nums = [1,None,2,3,None,None,5,None]
valid = 0
for x,i in enumerate(nums): 
        if i is not None:    
            valid = i
        else:
            nums[x] = valid
print(nums)

 

 
sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

set1 = set(sentence1.split())
set2 = set(sentence2.split())

print(sorted(set1 | set2))
print(sorted(set1 & set2))


 

 
n = int(input("enter a num : "))
primes = []

for num in range(n+1):
    if num > 1:
        print("num : ",num)
        for i in range(2,num):
            print("i : ",i)
            if num%i == 0:
                break
        else:
            print("appending : ", num)
            primes.append(num)

print(primes)
 

k = int(input("enter a num "))
for i in range(k):
    for j in range(k):
        if i + j == k:
            print(i,"+ ",j)



