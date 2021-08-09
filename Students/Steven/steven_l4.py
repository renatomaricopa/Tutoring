import random
# function definition with the wordlist as an argument/parameter
def getRandomWord(wordList):
    choice = random.choice(wordList)
    return choice
  
def displayBoard(userBlanks, missedLetters, numberOfGuesses):
    # join every element int the list into a string separated by no string.
  	showBlanks = "".join(userBlanks)
    print(showBlanks)
    print(f"Missed Letters: {' '.join(missedLetters)}")
    print(f"Number of Guesses: {numberOfGuesses}")

def getGuess(guessedAlready):
    while True:
    	guess = input("Enter a letter: ")
        if len(guess) == 1 and guess.isalpha() and guess not in guessedAlready:
        	return guess
        else print("Sorry, enter a valid letter")
def main()
	# square brackets to initialize list
    wordList = ["apple", "computer"]
    secretWord = getRandomWord(wordList)
    userBlanks = ["_ " for i in range(len(secretWord))]
    guessedAlready = []
    missedLetters = []
    numberOfGuesses = 6
	while numberOfGuesses > 0:
        displayBoard(userBlanks, missedLetters, numberOfGuesses)
        # game logic
        
        
        
