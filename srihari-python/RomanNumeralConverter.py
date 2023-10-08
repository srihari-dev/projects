dec = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
rom = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
n =  int (input ("Enter the number ="))
roman= " "
for i  in range (len(dec)):
    m = n //dec[i]
    for j in range (m):
        roman +=rom[i]
    n = n % dec [i]
print (roman)
    
        
