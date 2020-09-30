from math import pi

def acc(v1, v2, t1, t2):
    a = (v2 - v1) / (t2 - t1)
    return a

print(acc(0, 10, 0, 20))

def calc (h, r =10):
    v = ((4 * pi * (r**3)) / 3) - (((pi * (h*2)) * ((3 * r) - h)) / 3)
    return v
    
print(calc(2))


def foo(): 
    global c
    c = 1
    return c 

foo() 
print(c)