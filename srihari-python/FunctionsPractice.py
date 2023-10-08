'''
def Change(P,Q=30):
    P=P+Q
    Q=P-Q
    print(P,'#',Q)
    return (P)
R=150
S=100
R=Change(R,S)
print(R,'#',S)
S=Change(S)'''
'***************************'
'''
num=1
def myfunc():
    num=10
    return num
print(num)
print(myfunc())
print(num)'''

'***************************'
'''
num=1
def myfunc():
    global num
    num=10
    return num
print(num)
print(myfunc())
print(num)'''

'**************************'
'''
def display():
    print('Hello',end=' *')
display()
print('there')'''

'*******************'
'''
def check(n1=1,n2=2):
   n1=n1+n2
   n2+=1
   print(n1,n2)
check()
check(2,1)
check(3)'''
'********************'
'''
def increment(n):
    n.append([4])
    return n
L=[1,2,3]
M=increment(L)
print(L,M) '''
'*********************'

'''
def increment(n):
    n.append([49])
    return n[0],n[1],n[2],n[3]
L=[23,35,47]
m1,m2,m3,m4=increment(L)
print(L)
print(m1,m2,m3,m4)
print(L[3]==m4)
'''
'****************************'
'''
def addEm(x,y,z):
    print(x+y+z)
    
def prod(x,y,z):
  return x*y*z

a=addEm(6,16,26)

b=prod(2,3,6)
print(a,b)'''
'************************'
'''
a=10
y=5
def myfun():
    y=a
    a=2
    print('y=', y, 'a=', a)
    print('a+y=', a+y)
    return a+y
print('y=', y, "a=",a)
print (myfun())
print("y=",y, "a=",a)'''
'******************************'
'''
def getones(num):
  #return the ones digit of the integer num
  onesdigit=num%10
  return onesdigit

s=getones(101)
print(s)'''
'*******************************'
'''
def multiply(number1,number2):
    answer =number1*number2
    print(number1,'times',number2,'=',answer)
    return(answer)
output=multiply(5,5)'''
'**********************************'
'''
def multiply(number1,number2):
    answer =number1*number2
    return(answer)
    print(number1,'times',number2,'=',answer)
    
output=multiply(5,5)'''
'**********************************'
'''
def dosomething(thelist):
    for element in thelist:
        print(element)
dosomething(['1','2','3'])
alist=['red','green','blue']
dosomething(alist)'''
'*********************************'
'''
def fun(d):
    for key in d:
        print('k:' ,key, 'value:', d[key])
d={'a':1, 'b':2,'c':3}
fun(d)'''
'*******************************'
'''
def update(x=10):
    x+=15
    print('x=',x)
x=20
update()
print('x=',x) '''

'*******************************'
'''
def fun(message,num=1):
    print(message * num)
fun('Python')
fun('Easy', 3)'''

'*********************************'
'''
def fun(s):
  k=len(s)
  m=""
  for i in range(0,k):
     if (s[i].isupper()):
       m=m+s[i].lower()
     elif s[i].isalpha():
        m=m+s[i].upper()
     else:
       m=m+"bb"
  print(m)
fun('scHool12@coM')'''
'**********************************'
'''
def increase(x):
   a=a+x
   return

a=20
b=5
increase(b)
print(a)'''
'**********************************'
'''
a=20
b=5
def increase(x):
   #a=100 
   a=a+x
   print(a)
   return a


increase(b)
print(a)'''
'******************'
'''
a = 20
def idk(a):
    #global a
    a=a+2
    #b = a+2
    return a
x = idk(a)
print(x)'''
'**********************'
'''
def switch(x,y):
  x,y=y,x
  print("inside switch:",end='')
  print("x=",x,"y=",y)
x=5
y=7
print("x=",x,"y=",y)
switch(x,y)
'''
print("x=",x,"y=",y)
