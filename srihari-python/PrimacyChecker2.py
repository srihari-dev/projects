n=int(input("Enter number"))
for i in range(2,n):
    if n%i==0:
        print(n,"Is not a prime number")
        break
    else:
        if i==n-1:
            print(n,"Is a prime number")
