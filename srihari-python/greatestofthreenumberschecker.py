#Program to determine the largest of three numbers
n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
n3=int(input("Enter third number"))
if n1>n2:
    if n3>n1:
        print(n3,"Is the greatest number")
    else:
        print(n1,"Is the greatest number")
if n1<n2:
    if n3>n2:
        print(n3,"Is the greatest number")
    else:
        print(n2,"Is the greatest number")
