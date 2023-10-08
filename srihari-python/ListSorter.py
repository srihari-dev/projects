#Program to manually sort a given list
l=eval(input("Enter List"))
for x in range(len(l)):
    for y in range(len(l)-x-1):
        if l[y]>l[y+1]:
            tempor=l[y]
            l[y]=l[y+1]
            l[y+1]=tempor
            print(l)
