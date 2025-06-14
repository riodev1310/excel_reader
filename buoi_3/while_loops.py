import random 

run = True

while run: 
    your = int(input("Your number: "))
    bot = random.randint(1, 3)
    
    if your > bot: 
        print("You win, end the game") 
        run = False
    elif your < bot:
        print("You lose, keep playing until you win")
    else:
        print("Draw, keep playing until you win")