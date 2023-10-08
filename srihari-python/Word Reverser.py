#Program to reverse a word that is given.
Word=(input("Enter a word."))
print("The reverse of",Word,"is:")
length=len(Word)
for x in range(-1,(-length-1),-1):
     print(Word[x],end=" ")
