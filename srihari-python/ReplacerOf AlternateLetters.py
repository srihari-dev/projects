s=input("enter word")
for x in range(len(s)):
    if x%2==0:
        print(s[x].upper(),end="")
    else:
        print(s[x],end="")

    
