l=eval(input("Enter List"))
b=tuple(l)
for x in range(1,len(l)):
    key=l[x]
    j=x-1
    while j>=0 and key<l[j]:
        l[j+1]=l[j]
        j=j-1
    else:
        l[j+1]=key
    print(l)
print(l,"Is the sorted list.")
print(list(b),"Is the unsorted list")
