s=input("Enter String")
d={}
for i in s:
    d.update({i:s.count(i)})
print(d)
