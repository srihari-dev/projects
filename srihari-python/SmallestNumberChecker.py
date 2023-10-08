small=smallest=0
for i in range(10):
    n=int(input("Enter a number"))
    if i==0:
        small=n
    elif i==1:
        if n<=small:
            smallest=n
        else:
            smallest=small
            small=n
    else:
        if n<smallest:
            small=smallest
            smallest=n
        elif n<small:
            small=n
print("The smallest number is",smallest)
print("The second number is",small)
    
