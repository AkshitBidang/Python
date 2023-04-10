def ch(x,y):
    if x>y:
        s=y
    else:
        s=x
    for i in range(1,s+1):
        if ((i%x==0) and (i%y==0)):
            h=i
    return h
a=int(input("Enter 1st number="))
b=int(input("Enter 2nd number="))
print("HCF =",ch(a,b))
