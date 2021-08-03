import random
import time

def intro():
    region = input("Pick a pokemon region!")
    print(f"You are in {region} region where you are about to get your first pokemon.")
    pokeball = int(input("There are three pokeballs in front of you. Choose wisely. (1, 2, or 3)"))
    while (pokeball > 3 or pokeball < 0):
  	    pokeball = int(input("Sorry the pokeball you wanted does not exist. Please choose number 1, 2 or 3!"))  
    return pokeball            
def get_pokemon(pokeball):
    all_pokemon = ["Pikachu"] * 40 + ["Squirtle"] * 50 + ["MewTwo"] * 10
    pokemon = random.choice(all_pokemon)
    print(f"The pokeball you chose: {pokeball}, got you a...", end="")
    time.sleep(2)
    print(pokemon)  

def ending():
    play_again = input("Thanks for playing! Congrats on your new pokemon! Do you want to play again? (yes or no)")
    if play_again == "yes":
        return True
    else: return False
                 
play_again = True
while play_again:
    pokeball = intro()
    get_pokemon(pokeball)
    play_again = ending()
print("Okay bye!")