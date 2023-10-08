#Program to determine the type of character
f=input("Enter any character")
if f>="a" and f<="z":
    print(f,"is a lowercase letter")
elif f>="A" and f<="Z":
    print(f,"is an uppercase letter")
elif f>="0" and f<="9":
    print(f,"is a digit")
else:
    print(f,"is a symbol")
