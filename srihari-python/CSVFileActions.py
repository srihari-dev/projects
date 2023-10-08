import csv
def write():
         f=open("StudentRecords.csv","w",newline='')
         dw=csv.writer(f)
         dw.writerow(["roll number","student","stream"])
         Ans="y"
         while Ans=="y":
               rollnum=int(input("Enter Roll Number"))
               name=input("Enter student name")
               stream=input("Enter stream")
               e=[rollnum,name,stream]
               g=dw.writerow(e)
               Ans=input("Do you wish to enter more records? (y/n)")
def read():
    fo=open("StudentRecords.csv","r")
    dr=csv.reader(fo)
    for i in dr:
        print(i)
    fo.close()

               
