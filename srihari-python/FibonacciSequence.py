term1=0
term2=1
l=term1
f=term2
n=int(input("Enter the number of terms in the fibonacci sequence you want to see."))
print("The fibonacci sequence is 0,1,",end="")
for x in range(n-2):
    term3=term1+term2
    term1=term2
    term2=term3
    print(term3,end=" ")


    
