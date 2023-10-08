import pickle
def write():
  f=open("binary.dat","wb")
  while True:
      e1=int(input("Enter student roll number"))
      e2=input("Enter student name")
      e3=input("Enter student department")
      r=[e1,e2,e3]
      pickle.dump(r,f)
      op=input("Do you wish to add more files? (y/n)")
      if op!="y":
          break
  f.close()
def read():
    f=open("binary.dat","rb")
    try:
        while True:
                 r=pickle.load(f)
                 print(r)
    except EOFError:
              f.close()
              
def delete(d):
    import os
    fr=open("binary.dat","rb")
    fo=open("temp.dat","wb")
    try:
        while True:
          l=pickle.load(fr)
          if l[2]!=d:
            pickle.dump(l,fo)
    except EOFError:
            fr.close()
    os.remove("binary.dat")
    os.rename("temp.dat","binary.dat")
      
      

