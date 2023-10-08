def Main():
    print("                         \t>>>Welcome to Arcade<<<")
    q=int(input("\t\tHit 1 for Numlock, 2 for Hand cricket and 3 for Wordle : "))
    if q==1:
        import random
        def Numlock():
            d=1
            print("""\n                                      Rules

    1.Once you start a random number will be generated from 10-99.
    2. You must choose which place digit you want to guess and input your guess for each of the two
    digits.
    3. You can trade guess for clues by pressing -
            -'q' for clue corresponding to range of the number.
            -'w' for clue corresponding to 1st digit
            -'e' for clue corresponding to 2nd digit
    The clue's should be inputed when choosing which digit you want to guess.
                                        You have 7 guesses, Good luck!""") 
            y=input("\n                               >>>HIT ENTER TO PLAY<<<")
            if y=="":
                Num=random.randint(10,99)
                
                i=list(map(int, str(Num)))
                
                z=str(Num)           
                while d<8:
                    d+=1
                    a=input("Would you like to guess the 1st or the 2nd Digit or have a clue :")
                    if a=="1":
                        b=(input("Your guess:"))
                        print("\n")
                        if b==z[0]:
                            print("\t\t\tCongrats on being right. You can guess 2nd digit now ")
                            print("\n")
                            while d<8:
                                d+=1
                                f=input("Your guess:")
                                print("\n")
                                if f==z[1]:
                                    print("\t\t\t\t    Congrats on finishing the game. ")
                                    d=9
                                elif f=="e":
                                    if i[1] in range (0,5):
                                        print("2nd digit is in range (0-4)")
                                    else:
                                        print("2nd digit is in range (5-9)")
                                else:
                                    print("Try again")
                        else:
                            print("Try again")
                    elif d==9:
                            break
                    elif a=="2":
                        c=(input("Your guess:"))
                        print("\n")
                        if c==z[1]:
                            print("\t\t\tCongrats on being right. You can guess 1st digit now ")
                            while d<8:
                                d+=1
                                q=(input("Input your guess (Or you can trade guess for clues) - "))
                                print("\n")
                                if q==z[0]:
                                    print("\t\t\t\t    Congrats on finishing the game. ")
                                    d=9
                                elif q=="w":
                                    if i[0] in range (1,5):
                                        print("1st digit is in range (1-4)")
                                    else:
                                        print("1st digit is in range (5-9)")
                                else:
                                    print("Try again")
                        else:
                            print("Try again")
                    elif a=="q":
                        if Num<25:
                                print("The number is < 25")
                        elif Num in range (25,51):
                                print("The number is in range of (25-50)")
                        elif Num in range (51,76):
                                print("The number is in range of (51-75)")
                        else:
                            print("The number is > 75")
                    elif a=="w":
                        if i[0] in range (1,5):
                            print("1st digit is in range (1-4)")
                        else:
                            print("1st digit is in range (5-9)")
                    elif a=="e":
                        if i[1] in range (0,5):
                            print("2nd digit is in range (0-4)")
                        else:
                            print("2nd digit is in range (5-9)")
                while 7<d<9:
                    d+=1
                    print("You lost ; The number was : " ,z)
            
                   
        Numlock()
        
        ask=input("\n\t\t\t\t Press enter to go back to homescreen : ")
        if ask=='':
            Main()
        else :
            print("\n\t\t\t\t     >>>> Have A Good Day :) <<<<")


        
    elif q==2:
        import random
        import sys
        rules=input("""                                          Python Cricket
    Rules:
    This is a 2 Player game simulation of Cricket. Each inning's comprises of 1 over(6 balls).There
    is a random number generated between 1 and 6 for each ball. The First Player will enter a
    number between 1 to 6 for each ball. If the number entered by the player and the number
    generated by the game are the same, then the player is out. If not, the number entered by the
    player is counted as runs scored. This is repeated for the 2nd player.To quit the game at any
    point of time, enter a number that is NOT IN THE RANGE OF 1 TO 6.

                                >>>Hit Enter to play<<<""")
        print("\n\n")
        P1=input("What is the name of the First player?")
        P2=input("and the Second player's?")

        PL1=P1.title()
        PL11=PL1+(",your Out")
        PL2=P2.title()
        PL22=PL2+(",your Out")

        P1=P1.capitalize()
        P1=P1+"'s Turn to Play"
        P2=P2.capitalize()
        P2=P2+"'s Turn to Play"
        print("\n\n")
        print("                                       First up is",PL1)
        score1=score2=score_copy=c=0

        for i in range(1,7):
            n=random.randint(1,6)
            k=""
            k="("+str(n)+")"
            print("Choice for ball",i,":",end='')
            ch=int(input(""))
            if ch<1 or ch>6:
                print("                                         THANK YOU FOR PLAYING")
                sys.exit()
            elif ch!=n:
                score1+=ch
                print("Score=",score1,"        ",k)
                c+=1
            elif ch==n:
                print("Score            ",k,"                 ",PL11,"""       
                                           1st INNINGS OVER
                                           """)
                break
        if c==6:
            print("                                         1st INNINGS OVER\n                                      ",P2)
        ch=c=0
        print("                              ",PL2,"needs to score",score1+1,"runs to win")
        for j in range(1,7):
            n=random.randint(1,6)
            k=""
            k="("+str(n)+")"
            print("Choice for ball",j,":",end='')
            ch=int(input(""))
            score_copy+=ch
            if ch<1 or ch>6:
                print("                                         THANK YOU FOR PLAYING")
                sys.exit()
            elif score_copy>score1:
                break
            elif ch!=n:
                score2+=ch
                print("Score=",score2,"        ",k)
                c+=1
            elif ch==n:
                break
        if c==6:
            print("\t\t\t                      MATCH OVER")

        if score1>score2:
            print("Score=",score2,"        ",k)
            print("\n\n                                   ",PL1,"WINS BY",score1-score2,"RUNS\n                                 Better Luck Next time",PL2)
            print("                                   THANK YOU FOR PLAYING")
        elif score1<score2:
            print("Score=",score2,"        ",k)
            print("\n\n                                   ",PL2,"WINS BY",score2-score1,"RUNS\n                                 Better Luck Next time",PL1)
            print("                                   THANK YOU FOR PLAYING")
        elif score1==score2:
            print("Score=",score2,"        ",k)
            print("                      MATCH OVER")
            print("\n\n                                           ","DRAW")
            print("                                    THANK YOU FOR PLAYING")
        
        ask=input("\n\t\t\t\t Press enter to go back to homescreen :  ")
        if ask=='':
          Main()
        else :
            print("\n\t\t\t\t     >>>> Have A Good Day :) <<<<")
    elif q==3:
        import random as r
        #import mysql.connector as mys
        #my=mys.connect(host='localhost',database='noel',user='root',password='my3qlP@ssword')
        #myc=my.cursor()
        print("\n\tWordle is a game where a word is generated and you must guess the word\n")
        print("""\t\t\t\t\tRULES\n
        1)The word you input must be 5 letters long
        2)If a letter in your word is in the original word and is in the correct position, the letter will appear in [].
            Example : Word -> THYME
                      Your guess -> SHINE
                      Output -> S H I N [E]
        3)If a letter in your word is in the original word but not in the same position, the letter will appear in ().
            Example : Word -> THYME
                      Your guess -> ANGRY
                      Output -> {M} O {T} {T} O
        4)You have 6 attempts to guess the word.
        5)Finish the game by guessing the word before you run out of attempts.\n""")
                      

        words=['PAGER', 'DOUBT', 'THYME', 'ALPHA', 'BOOZE', 'TIBIA', 'LOFTY', 'THEME', 'CLASS', 'LEERY', 'TAUNT', 'WHOOP',
           'INTER', 'GULLY', 'CHARM', 'FUNGI', 'PRIZE', 'ONSET', 'CHIEF', 'GAUZE', 'RUDER', 'IRONY', 'CLOWN', 'NEEDY',
           'WOVEN', 'MERIT', 'WASTE', 'TREAT', 'SHRUG', 'TWANG', 'TWICE', 'GRUEL', 'POKER', 'KHAKI', 'HUNKY', 'LABEL',
           'GLEAN', 'CLING', 'PATTY', 'UNFIT', 'SMEAR', 'ALIEN', 'BUGGY', 'RHYME', 'YOUTH', 'COYLY', 'QUART', 'CRAMP',
           'BLUFF', 'STOMP', 'MOTTO', 'CINCH', 'ELOPE', 'POWER', 'MIDGE', 'TRYST', 'APHID', 'TRITE', 'ANGRY', 'FLOCK',
           'WACKY', 'ROOMY']
        y=r.randint(0,62)
        a=words[y]
        b=list(a)
        print (b)

        start=input("\t\t    A word has been generated, press enter to start")
        if start=="":
            #num=6
            i=0
            
            while i<6:
                print("\n",i)
                i=i+1
                
                #print(num)
                guesss=input("\nInput your guess : ")
                guess=guesss.upper()
                
                lg=list(guess)
                if len(lg)!=5:
                    print("INVALID INPUT. INPUT MUST HAVE 5 CHARACTERS/LETTERS")
                    print(i)
                    i=i-1
                    print(i)
                elif len(lg)==5:
                    if lg==b:
                            print("""\n\t\t\t\t  >>> YOU WIN :) <<<""")
                            print("\t\t\t\t  THE WORD WAS""",a)
                            break
                        
                    for j in range(0,5):
                        
                        if lg[j]==b[j]:
                            lg[j]="["+b[j]+"]"
                        elif lg[j] in b:
                            lg[j]="{"+lg[j]+"}"
                    gw=""
                    for g in lg:
                        gw+=g
                        gw+=" "
                    print("\n",gw)
                if i==6 and lg!=b:
                    print ("""\n\t\t\t\t    >>> YOU LOSE :( <<<""")
                    print("""\t\t\t\t   THE WORD WAS""",a)
        ask=input("\n\t\t\t Press enter to go back to homescreen :  ")
        if ask=='':
          Main()
        else :
            print("bruh type something")
           
