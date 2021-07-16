# user_input = input()
# print(user_input)

minimum = 7
maximum = 15
print("Hello! What is your name?")
name = input()
# string formatting (or interpolation)
# Key: %s is for a string, %f is for a float, %i is for an integer
# https://stackabuse.com/python-string-interpolation-with-the-percent-operator
print("Ok %s, I'm thinking of a number between %i and %i. Take a guess." % (name, minimum, maximum))


# Game: Guess the number
# 
# Computer: Hello! What is your name? 
# User: Eugene
# Computer: Ok Eugene, I'm thinking of a number between 1 and 20. Take a guess.
# User: 10
# Computer: Your guess is too high.
# User: 4
# Computer: Your guess is too high.
# User: 4
# Computer: Your guess is too high.
# User: 4
# Computer: Your guess is too high.
# User: 4
# Computer: Your guess is too low.
# 
# if the user guesses 6 times:
# Computer: Sorry, you lost. You took too many turns.
# 
# if less than 6 times and they guessed it:
# Computer: Perfect. You won! You took 3 turns. 








