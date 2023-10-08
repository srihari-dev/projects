#Program to select numbers out of an inputted list and make new list
n=[]
s=eval(input("Enter list"))
l=s
for element in s:
    if str(element).isalpha()==True:
        continue
    else:
        s.remove(element)
        n.append(element)
print(n,"contains the set of numbers in the list",l)
        
