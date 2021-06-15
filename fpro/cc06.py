import random
file = open("file00.txt", 'w')
file.write(str(random.random()))
file.close()

file = open("file00.txt", 'r')
print(file.read())
file.close()

file = open("file00.txt", 'a')
file.write("appended stuff")
file.close()

file = open("file00.txt", 'r')
print(file.read())
file.close()

