import pickle
import os
f=open("Binary.dat","wb")
fo=open("Temp.dat","wb")
Ans="y"
while Ans=="y":
    x=int(input("Enter Roll Number"))
    y=input("Enter Name")
    z=input("Enter Department")
    e=[x,y,z]
    pickle.dump(e,f)
    Ans=input("Do you wish to continue adding? (y/n)")
f=open("Binary.dat","rb")
try:
    while True:
        r=pickle.load(f)
        print(r)
except EOFError:
    f.close
def delete(x):
    try:
        while True:
            if e[2]!=x:
                pickle.dump(e,fo)
                os.rename("Temp.dat","Binary.dat")
                os.remove(f)
    except EOFError:
        f.close()
        fo.close()
