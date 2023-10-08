#Program to calculate simple interest on a certain principal amount of money
P=float(input("Enter the principal amount on which the simple interest is to be calculated:"))
R=float(input("Enter the rate percentage per annum on which the simple interest is to be calculated:"))
T=int(input("Enter the time in years over which the interest is to be determined.:"))
I=P*R*T/100
print("The simple interest over a period of",T,"years is",I,"rupees")
