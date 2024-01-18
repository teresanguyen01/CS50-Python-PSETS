import random

def main():
    random_guessing_game()

def random_guessing_game(): 
    guess = 0
    levels = (input("Level: "))

    while levels.isalpha(): 
        levels = (input("Level: "))
    
    while (int(levels)) < 0: 
            levels = (input("Level: "))
            
    guessing_number = random.choice([1,int(levels)])
    

    guess = (input("Guess: "))

    while guess.isalpha():
        guess = (input("Guess: "))
    
    while (int(guess) < 0):
        guess = (input("Guess: "))

    if (int(guess) == guessing_number): 
        print("Just right!")
    else: 
        while int(guess) != guessing_number:
            if int(guess) > guessing_number: 
                print("Too large!")
                guess = int(input("Guess: "))
            else: 
                print("Too small!")
                guess = int(input("Guess: "))
    
    print("Just right!")

main()
        
