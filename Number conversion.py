def b(a):
    return bin(a)
def o(a):
    return oct(a)
def h(a):
    return hex(a)
a=int(input("Enter a number="))
print("Entered number in the following formats:-\n1.Binary=",b(a),"\n2.Octal=",o(a),"\n3.Hexadecimal=",h(a))