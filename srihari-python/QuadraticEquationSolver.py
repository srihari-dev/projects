#Program to uncover the roots of a quadratic equation
import math 
print("Please provide the values of the quadratic coefficients of the equation you want to solve.")
print("ax^2+bx+c=0")
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
print("the equation is ",a,"x^2+",b,"x+",c,"=0")
r=-c/b
D=b**2-4*a*c
if D<0:
    print("The roots are imaginary")
else:
    r1=(-b+math.sqrt(D))/2*a
    r2=(-b-math.sqrt(D))/2*a
    if a==0:
        print("The equation is linear, the solution is",r)
    else:
         if D<0:
                 print("The roots are imaginary")
         elif D==0:
                    print("The roots are real and equal, and they are both equal to",-b/(2*a))
         else:
              print("The roots are real and distinct. Their values correspond to",r1,",",r2)
    
