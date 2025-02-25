import random

#Randon number is generated between 1 to 3
#1 for snake, 2 for water, 3 for gun
comp=random.randint(1,3)

#This is ASCII svg arts
snake="""
      _______
     / _   _ \\
    / (.) (.) \\
   ( _________ )
    \`-V-|-V-'/
     \   |   /
      \  ^  /
       \    \\
        \    `-_
         `-_    -_
            -_    -_
            
    """    

pistol="""
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX /
 / XXXXXX /
(________(                
 `------'            
  """
water="""
            .........                        
    ....::===--:..                      
  ....--====----::.                     
  ...==-+-=:....::.                     
....-++=*=:..                           
....-+=-=+.:..                          
.:::-=-:::-:.....                     ..
=====-=-+=-:-..:...                ....:
**#***+==+====--=..-...............:--=+
+++++++***++**+=+===+=-:....:-:.:-=+++++
:::::::----================++======---::
.............:::::::::::::::::::........
"""
#The main program starts here 
welcome="""
          *WELCOME*
             TO
     <>SNAKE WATER GUN<>
            GAME"""
print(welcome)

ch="s"

while ch=='s' or ch=='S':

    print("1️⃣  SNAKE \n2️⃣  WATER \n3️⃣  GUN")
    for i in range(1,4):  
     userch=int(input("Enter your choice:"))
    
     if userch==1:
        print(snake)
     elif userch==2:
        print(water)
     elif userch==3:
        print(pistol)
     else:
        print("Invalid choice")
        break
    
     if(comp==1):
        print(snake)
        if(userch==1):
            print("TIE")
        elif(userch==2):
            print("YOU LOOSE")
        elif(userch==3):
            print("YOU WIN")
     elif(comp==2):
        print(water)
        if(userch==1):
            print("YOU WIN")
        elif(userch==2):
            print("TIE")   
        elif(userch==3):
            print("YOU LOOSE")
     elif(comp==3):
        print(pistol)
        if(userch==1):
            print("YOU LOOSE")
        elif(userch==2):
            print("YOU WIN")
        elif(userch==3):
            print("TIE")

    print("\n\n\n")
    ch=input("To CONTINUE enter 'S' or 'Q' to QUIT: ")
    if(ch=='Q' or ch=='q'):
        print("\n\n\nTHANK YOU FOR PLAYING 😊🔥🐍\n\n\n")     
