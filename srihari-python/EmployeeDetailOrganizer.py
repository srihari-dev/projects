#Program to organize details of an employee
Empname=[]
Empdepartment=[]
Empsalary=[]
d={}
n=int(input("Enter number of employees"))
for i in range(n):
    x=input("Enter Name")
    Empname.append(x)
    y=input("Enter department")
    Empdepartment.append(y)
    z=input("Enter salary")
    Empsalary.append(z)
for x in range(len(Empname)):
     d[Empname[x]]=Empdepartment[x],Empsalary[x]
print(d)

