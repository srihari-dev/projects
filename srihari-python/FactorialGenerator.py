#Program to discover factorial of a number
n=int(input("Enter a number "))
if n<0:
    print("The factorial of a negative number is nonexistent")
elif n==0:
    print("The factorial of 0 is 1")
else:
    f=1
    for i in range(1,n+1,1):
        f=f*i
    print("The factorial of",n,"is",f)
    
