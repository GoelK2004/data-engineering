"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Your task is to determine the winner of the game and their score.

Function Description
Complete the minion_game in the editor below.
minion_game has the following parameters:
	string string: the string to analyze
Prints
	string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
"""

def minion_game(string):
    length = len(string)
    stuart_score = 0
    kevin_score = 0
        
    for i in range(length):
        if string[i] in "AEIOU":
            kevin_score += length - i
        else:
            stuart_score += length - i
    
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

"""
Thought Process:
	Example: BANANA
	We have to count all the substrings either starting with vowel or consonants for Kevin and Stuart respectively.
    When we are at letter say, B, we can count the remaining alphabets including B, that counts the total substring that can be made from the letter B.
    All the occurences will be taken into account with this method.
    
    If we are at: ANA
    It will be count twice, first, when we are at index 1 and second, at index 3.
"""