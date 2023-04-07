a=int(input("Enter a positive number="))
if (a==2):
    print("The entered number is the smallest prinme number.")
else:
    for i in range(2,int(a/2)+1):
        if (a%i==0):
            print("The number is not prime.")
            break
        else:
            print("The number is prime.")