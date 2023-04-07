import math
a=int(input("Enter a number to check whether it is armstrong or not="))
c=0
t=a
z=a
arm=0
while t>0:
    t=t//10
    c=c+1
while z>0:
    r=z%10
    arm=arm+pow(r,c)
    z=z//10
if arm==a:
    print(a,"is armstrong number.")
else:
    print(a,"isn't armstrong number.")