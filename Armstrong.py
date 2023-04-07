import math
a=int(input("Lower bound of interval="))
b=int(input("Upper bound of interval="))
print("Armstrong numbers in the interval are\n")
for i in range(a,b+1):
    arm=0
    t=i
    z=i
    c=0
    while t>0:
        t=t//10
        c=c+1
    while z>0:
        r=z%10
        arm=arm+pow(r,c)
        z=z//10
    if arm==i:
        print(i)