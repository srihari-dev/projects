#Program to count the number of digits in a number
num=int(input("Enter the number whose digits must be counted"))
f=num
n=0
while num>0:
    num=num//10
    n=n+1
print("The number",f,"has",n,"digits")
