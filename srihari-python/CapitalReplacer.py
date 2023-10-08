s=input("Enter word")
c=input("Enter character")
n=c
c=c.upper()
C=c
for x in range(len(s)):
    if s[x]==n:
        s=s.replace(s[x],C)
print(s)

