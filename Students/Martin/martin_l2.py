# // Copy and paste your work, or start typing.

class Golf:
# __init__ is a method of the class that initializes variables for this class
    def __init__(self, holeNumber, score, par):
        self.holeNumber = holeNumber
        self.score = score
        self.par = par
    def evaluateAndDisplayScore(self, userScore):
        self.score = userScore
        if self.score < self.par:
            print('You scored Under Par with a score of ' + str(self.score) + ' on hole # ' + str(self.holeNumber) + ' with a par of ' + str(self.par))
        elif self.score > self.par:
            print('You scored Over Par with a score of ' + str(self.score) + ' on hole # ' + str(self.holeNumber) + ' with a par of ' + str(self.par))
        elif self.score == self.par:
            print('You scored At Par with a score of ' + str(self.score)  + ' on hole # ' + str(self.holeNumber) + ' with a par of ' + str(self.par))

# Initializaing the holes (before the user input) AKA creating the golf course
userScore = 0
hole1 = Golf(1, userScore, 3)
hole2 = Golf(2, userScore, 4)
hole3 = Golf(3, userScore, 5)

hole = int(input('Enter the hole number '))
userScore = int(input('Enter your score '))

if hole == 1:
    hole1.evaluateAndDisplayScore(userScore)
elif hole == 2:
    hole2.evaluateAndDisplayScore(userScore)
elif hole == 3:
    hole3.evaluateAndDisplayScore(userScore)
