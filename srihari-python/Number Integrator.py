#To obtain the sum of the digits of a given number
n=int(input("Enter the number"))
sum=0
while n>0:
    a=n%10
    sum=sum+a
    n=n//10
print("The sum of the digits is equal to ",sum)
