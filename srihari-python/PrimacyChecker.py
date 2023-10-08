#Program to check if a number is prime
num=int(input("Enter a number to check if it's prime: "))
for i in range(2,num,1):
    x=num%i
    if x==0:
        print(num,"is not a prime number, having factor:",i)
        break
else:
    print(num,"is a prime number")
