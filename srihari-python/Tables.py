#Program to write multiplication tables
n=int(input("Enter a number "))
if n==0:
    print("The table of 0 is simply 0x0=0")
else:
    for i in range(1,11,1):
        h=n*i
        print(n,"x",i,"=",h)
