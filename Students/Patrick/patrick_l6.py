#Function 1: Call this 3 times: getScore(score_type), takes the string of which score it is, returns 1 score
#Function 2: Call this once: averagesScores(score1, score2, score3), takes 3 scores, returns average of all scores
#Function 3: Call this once: averageHighest(score1, score2, score3), takes 3 scores, returns average of 2 highest scores

# Function definition for Function 1
def get_score(score_type):
    # string concatenation
    score = float(input("Please enter your " + score_type + " score between 0 and 100: "))
    while not (score >= 0 and score <= 100):
        score = float(input("Please enter your " + score_type + " score between 0 and 100: "))
    return score
# Function definition for Function 2
def get_average(score1, score2, score3):
	return (score1 + score2 + score3) / 3

# Function definition for Function 3
def get_highest_average(score1, score2, score3):
    score_list = sorted([score1, score2, score3])
    return (score_list[1] + score_list[2]) / 2
  
# Function calls for Function 1
score1 = get_score("first")
score2 = get_score("second")
score3 = get_score("third")

# Function call for Function 2
average_score = get_average(score1, score2, score3)

# Function call for Function 3
average_highest_score = get_highest_average(score1, score2, score3)

# Print out both average scores
print("Your average of you 3 scores is: " + str(average_score))
print("The average of your 2 highest scores is: " + str(average_highest_score))

# Function 1: Input/Parameter/Argument is 1 string, Output/Returns number of uppercase letters (1 integer)
# Function 2: Input/Parameter/Argument is 1 string, Output/Returns number of lowercase letters (1 integer)
# Function 3: Input/Parameter/Argument are upper_count, lower_count which are 2 integers, Output/Returns nothing! 
# Function definition for Function 1

def count_upper_letters(phrase):
    upper_count = 0
    for character in phrase:
        if character.isupper():
        	upper_count += 1
    return upper_count
	
# Function definition for Function 2
def count_lower_letters(phrase):
    lower_count = 0
    for character in phrase:
        if character.islower():
            lower_count += 1
    return lower_count
# Function definition for Function 3
def display_counts(upper_count, lower_count):
    print("Your phrase has " + str(upper_count) + " uppercase letters and " + str(lower_count) + " lowercase letters.")
# input
phrase = input("Enter any phrase: ")
# Function calls for Function 1
upper_count = count_upper_letters(phrase)
# Function call for Function 2
lower_count = count_lower_letters(phrase)
# Function call for Function 3
display_counts(upper_count, lower_count)
























