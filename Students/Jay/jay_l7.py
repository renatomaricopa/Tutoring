import random
import time
def intro():
    all_pokemon=["Pikachu"]*20+["Pidgeot"]*60+["Mew"]*5
    pokemon=random.choice(all_pokemon)
    print("You are currently walking through tall grass")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("... and you encounter a "+pokemon+"! Don't waste your pokeballs! You can catch it! ")
    choice=input("Wanna ignore and keep walking, go home, or catch it (keep walking, go home, catch it)?\n")
    return choice, pokemon
def make_choice(choice, pokemon, pokeballs):
    #This function focus on what to do when the p layer insert a choice.#
    pokedex={"Pikachu":25,"Pidgeot":50,"Mew":10}
    if choice == 'keep walking' or choice == 'ignore':
        return True
    elif choice == 'catch it':
        percentages=pokedex[pokemon]*[True]+(100 - pokedex[pokemon])*[False]
        caught=random.choice(percentages)
        print("You throw the pokeball and...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        if caught:
            print("YAAAAAAAAAAAAAY!!!! YOU CAUGHT IT!!!")
        else:
            print("OH NO. IT GOT OUT!")
        decision = input('Wanna keep walking or go home?')
        if decision == "keep walking":
            return True
        else:
            return False
    else:
        return False


print("Aloha! Welcome to the aloha region!")
decision = True
while decision:
    
    pokeballs = 10
    choice, pokemon=intro()
    decision= make_choice(choice, pokemon, pokeballs)
print("You walk home and go to sleep.")
time.sleep(1)
print("zzz")
time.sleep(1)
print("zzzzzzzzz")
time.sleep(2)
print("You are fast asleep. Goodnight!")



