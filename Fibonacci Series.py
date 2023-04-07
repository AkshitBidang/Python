#Using for loop
a=int(input("Enter the number of terms you want for Fibonacci series="))
x=0
y=1
print("The series is\n",x,y,end=" ")
for i in range(2,a):
    z=x+y
    print(z,end=" ")
    x=y
    y=z
#Using while loop
a=int(input("\nEnter the number of terms you want for Fibonacci series="))
x=0
y=1
print("The series is\n",x,y,end=" ")
while(a>2):
    z=x+y
    print(z,end=" ")
    x=y
    y=z
    a=a-1