# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# 1. Create a class called "Golf"
# 2. The class is gonna contain 3 attributes: par, score, holeNumber
#
# 3. Create three objects: each object is going to be a hole (1,2,3) (3,4,5) score = 0
#
# 4. Grab user input (the user input will be their score)
#       e.g. For hole 1, what score did you get?
#
# 5. Once we have the scores each hole, update our score in our object, display whether they had a score that was under par, over par, or at par.
#
# 6. This class is only going to have 1 method: evaluateAndDisplayScore(userScore):
#       update the score value and print whether the user got under par, over par, or at par for their score.
class Golf:
    def __init__(self, par, score, hole):
        self.par = par
        self.score = score
        self.hole = hole

    def evaluateAndDisplayScore(self, holeScore):
        self.score += holeScore
        if self.score < self.par:
            print("You scored under par")
        elif self.score == self.par:
            print("You scored at par")
        else:
            print("You scored over par")



def main():
    # initialization
    hole1 = Golf(3, 0, 1)
    hole2 = Golf(4, 0, 2)
    hole3 = Golf(5, 0, 3)
    holeScore1 = int(input("What score did you get for hole 1? "))
    holeScore2 = int(input("What score did you get for hole 2? "))
    holeScore3 = int(input("What score did you get for hole 3? "))
    hole1.evaluateAndDisplayScore(holeScore1)
    hole2.evaluateAndDisplayScore(holeScore2)
    hole3.evaluateAndDisplayScore(holeScore3)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

