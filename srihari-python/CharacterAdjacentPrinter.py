#Program to input letters of a string contiguously approaching the centre
s=input("enter a word")
for x in range(len(s)):
    print(s[x],end="                             ")
    print(s[len(s)-1-x])
