#Program to execute desired operations on chose no.'s
n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
op=input("Enter the operator that you want to execute on the numbers")
a=n1+n2
b=n1*n2
c=n1-n2
d=n1/n2
if op==("+"):
    print(a)
elif op==("-"):
    print(c)
elif op==("x") or op==("*"):
    print(b)
elif op==("/"):
    print(d)
else:
    print("Invalid operator")
    
