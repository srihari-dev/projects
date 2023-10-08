evenlist=[]
oddlist=[]
for i in range(5):
    n=int(input("Enter number"))
    if n%2==0:
        evenlist+=str(n)
    elif n%2==1:
        oddlist+=str(n)
print(evenlist,oddlist)
        
