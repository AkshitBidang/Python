def lcm(x,y,z):
    if x>y:
        greater=x
    elif(y>z):
        greater=y
    else:
        greater=z
    while True:
        if (greater%x==0) and (greater%y==0) and(greater%z==0):
            l=greater
            break
        else:
            greater=greater+1
    return l
a=int(input("Enter 1st number="))
b=int(input("Enter 2nd number="))
c=int(input("Enter 3rd number="))
d=lcm(a,b,c)
print("LCM of",a,",",b,"and",c,"=",d)