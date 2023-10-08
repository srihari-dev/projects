#Program to determine the distance between two points on the cartesian plane
import math
x1=int(input("Enter first x co-ordinate"))
y1=int(input("Enter first y co-ordinate"))
x2=int(input("Enter second x co-ordinate"))
y2=int(input("Enter second y co-ordinate"))
d=math.pow((math.pow(x2-x1,2))+(math.pow(y2-y1,2)),(1/2))
print("The distance between the given two points (",x1,",",y1,") and (",x2,",",y2,") is",d,"units")
