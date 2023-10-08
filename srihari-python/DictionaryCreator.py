#Program to hard-code a dictionary
n=int(input("Enter the number of elements of the desired dictionary: "))
d={}
for i in range(n):
    Key=input("Enter Key")
    Value=input("Enter Value")
    d.update({Key:Value})
print(d)
