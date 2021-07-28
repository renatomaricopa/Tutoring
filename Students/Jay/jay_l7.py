import random
import time
def intro():
    all_pokemon=["Pikachu"]*20+["Pidgeot"]*60+["Mew"]*5
    pokemon=random.choice(all_pokemon)
    print("Aloha! Welcome to the aloha region! Get it? You are currently walking through tall grass and you encounter a "+pokemon+"! Don't waste your pokeballs! You can catch it! ")
    choice=input("Wanna ignore and keep walking, go home, or catch it?")
    return choice, pokemon
def decision(choice, pokemon, pokeballs):
    #This function focus on what to do when the p layer insert a choice.#
    pokedex={"Pikachu":25,"Pidgeot":50,"Mew":10}
    if choice == 'walk' or choice == 'ignore':
        return True
    elif choice == 'catch':
        percentages=pokedex[pokemon]*[True]+(100 - pokedex[pokemon])*[False]
        caught=random.choice(percentages)
        if caught:
            print("YAAAAAAAAAAAAAY!!!! YOU CAUGHT IT!!!")
        else:
            print("WWWHHHYYYYY????? WHY, GET IN INSIDE THE POKEBALL!!!! ")
        decision = input('Wanna continue walking or go home?')
        if decision == "walk":
            return True
        else:
            return False
    else:
        return False

decision = True

while decision:
    pokeballs = 10
    choice, pokemon=intro()
    decision=decision(choice, pokemon)




