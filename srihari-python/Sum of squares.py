#Program to determine sum of squares
r=0
n=int(input("enter the number of natural numbers whose sum of squares is to be determined"))
for i in range(1,n+1,1):
      r=r+i**2
print("The sum of the first",n,"natural numbers can be declared to be",r)
