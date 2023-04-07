a=int(input("Enter the range for calculating series="))
s=0
print("Number of series=")
for i in range(1,a+1):
    print(i)
    s=s+i
print("Sum of the digits of the series=",s)