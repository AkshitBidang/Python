a=int(input("Enter the value of a="))
b=int(input("Enter the value of b="))
c=int(input("Enter the value of c="))
d=(b**2)-(4*a*c)
if d>0:
    r1=(-b+(d**0.5))/(2*a)
    r2=(-b-(d**0.5))/(2*a)
    print("Roots are real and distinct. R1=",r1,"R2=",r2)
elif d==0:
    r1=(-b+(d**0.5))/(2*a)
    r2=(-b-(d**0.5))/(2*a)
    print("Roots are real and equal. R1=",r1,"R2=",r2)
else:
    r1=(-b+(d**0.5))/(2*a)
    r2=(-b-(d**0.5))/(2*a)
    print("Roots are imaginary. R1=",r1,"R2=",r2)