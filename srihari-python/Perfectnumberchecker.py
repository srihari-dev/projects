#Program to check if a number is perfect
n=int(input("Enter the number to be processed"))
print("processing",end="")
for i in range(100):
    print(".",end="")
a=0
for x in range(1,n):
    if n%x==0:
        a+=x
if a==n:
    print("The number is perfect.")
else:
    print("The number isn't perfect")
