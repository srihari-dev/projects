#Program to determine if a number is an Armstrong number
num=int(input("Enter the number:"))
f=num
s=0
while num>0:
    a=num%10
    s=s+a**3
    num=num//10
if s==f:
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong number")
