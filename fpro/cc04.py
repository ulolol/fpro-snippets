def bmi(w,h):
    res = w/h**2
    return res


W = int(input('enter weight in Kgs'))
H = int(input('enter height in Meters'))
R = bmi(W,H)
print(R)
