import math
a = int(input("enter (a): "))
b = int(input("enter (b): "))
c = int(input("enter (c): "))
delta = b*b - 4 * a * c
dstr = str(delta)

print("Δ= " +  dstr)

num = int(input("please enter Δ again: "))
suqrt = math.sqrt(num)
sqrt = str(suqrt)
print ("√Δ= " + sqrt)
sfqrt = float(delta)
first_x = - 1 * b + sfqrt \ 2 * a
second_x = - 1 * b -  sfqrt \ 2 * a
print (first_x + "  " + second_x)
