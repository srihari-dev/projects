#Program to organize marks
d1={}
d2={}
d3={}
for n in range(3):
    r=int(input("Enter marks for student 1 in subject"))
    d1[n+1]=r
for n in range(3):
    r=int(input("Enter marks for student 2 in subject"))
    d2[n+1]=r
for n in range(3):
    r=int(input("Enter marks for student 3 in subject"))
    d3[n+1]=r
D={}
D["Student 1"]=d1
D["Student 2"]=d2
D["Student 3"]=d3
print(D)
for i in D:
    print("Name")
    print(i)
    print("Subject","\t","Marks")
    for x in D[i]:
        print(x,"\t",D[i][x])

        
          
