
import random
import time

    
def intro():
    region = input("Pick a pokemon region! (galar, somethingElse)")
    print("You are in {} region where you are about to get your first pokemon. There are 3 choices. \nOne is very strong, another is very terrible, and the other is super cute. chooese wisely.(1 or 2 or 3)".format(region))
def pick_pokemon():
    pokeball = input()
    pokeball=int(pokeball)
    something_pokemon=["Pikachu"] * 30 + ["Magikarp"] * 60 + ["Lugia"] * 10
    galar_pokemon=["Pikachu"] * 30 + ["Magikarp"] * 60 + ["Lugia"] * 10
    pokemon = random.choice(galar_pokemon)
    print(' You got...')
    time.sleep(2)
    if pokeball != 1 and pokeball != 2 and pokeball != 3:
        print('Hey you didn\'t choose a valid pokeball.')
    elif pokeball == 2:
        print('...')
        time.sleep(1.5)
        print('a cute pikachu!! Awww, pika pika!')
    elif pokeball == 1:
        print('Aww, you got a magikarp, though you evolve it to a powerful gyrados! Good luck doing that!')
    else:
        print('...')
        time.sleep(4.7)
        print('OMG!!!YOU GOT A LUGIA!!! YOU\'RE SO LUCKY!!!!!!!!!')
play_again='yes'
while play_again=='yes':
    intro()
    pick_pokemon()
    play_again=input('Wanna play again?(yes or no)')