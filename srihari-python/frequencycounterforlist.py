l=eval(input("Enter list"))
d={}
count=0
for i in l:
    for j in l:
        if i==j:
            count+=1
    d[i]=count
    count=0
print(d)
    
