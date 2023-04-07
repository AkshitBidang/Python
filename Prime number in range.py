lb=int(input("Enter the lower bound of range="))
ub=int(input("Enter the upper bound of range="))
print("The prime numbers in given range are\n")
for i in range(lb,ub+1):
    for j in range(2,i):
        if (i%j)==0:
            break
    else:
        print(i)