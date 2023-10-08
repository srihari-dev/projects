f=open("lile.txt","w")
l=[]
while True:
    x=input("Enter Student name")
    y=input("Enter Student interest")
    z=input("Enter student department")
    l.append(x+"\n")
    l.append(y+"\n")
    l.append(z+"\n")
    y=input("Enter more records? (y/n)")
    if y!="y":
        break
f.writelines(l)
f.close()
fo=open("lile.txt","r")
x=fo.readlines()
for r in x:
    print(r)


