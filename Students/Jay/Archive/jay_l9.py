HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
 
import random
# function definition with the wordlist as an argument/parameter
def getRandomWord(wordList):
    choice = random.choice(wordList)
    return choice
  
def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)], end="\n\n")
    print("Missed Letters:", end="")
    for letter in missedLetters:
        print(letter, end=" ")
    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:] # _p___
    for letter in blanks: 
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True: 
        guess = input("Enter a letter: ")
        if len(guess) == 1 and guess.isalpha() and guess not in alreadyGuessed:
            return guess
        else: print("Sorry, enter a valid letter")

def playAgain():
    # returns true if player wants to play again; otherwise false.
    return input("Do you want to play again? (yes or no)").lower().startswith('y')

# Initialize the game (word list, game name, secret word, initiailize variables)
words = ["apple", "python", "awesome", "computer", "lazer", "dictionary", "intelligence", "artificial"]
print("H A N G M A N")
missedLetters = ""
correctLetters = ""
secretWord = getRandomWord(words)
gameIsDone = False
while missedLetters:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters += guess    
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == 6:
            print("Sorry you lost!")
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
    # userBlanks = ["_ " for i in range(len(secretWord))]
    # numberOfGuesses = 6
    # while numberOfGuesses > 0:
    #     displayBoard(userBlanks, missedLetters, numberOfGuesses)
    #     # game logic


#
#1. We are going to use secret_word = random.choice(words)(with  on our words list to get a random word! Also remember to create a used word list!
#2. Print out the word "HANGMAN" so the user knows what game we are playing!
#3. Next, print out the actual hangman person. And also create a string with the blanks for the word. There should be as many blanks ("_") as the length of the word!
#4. while the man hasn't been fully hanged. man = 0 While man != 6: 
#5. Ask the user for a letter!
#6. if letter in used word list:
#print("You already used that letter! Please use a letter you haven't used!")
#     7. elif input isn't a letter from the secret word :
#8.print a body part 
#9. else:     
#10. fill in the blanks inside our word!
#11.if the user guessed the whole secret word:
#12. print the picture and the secret word that they guessed
#13. print("Congratulations you won!")
#14. break or make man = 6
#15. if man == 6:
#16. print("AAWWWWW.You lost")

