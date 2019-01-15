'''
Created on Jan 15, 2019

@author: mingw
'''
import random

def roll(sides=6):
    num_rolled = random.randint(1, sides)
    return num_rolled

def main():
    sides = input("How many sides does your dice have?")
    while(sides.isdigit()==False):
        sides = input("You didn't give an number, try again. How many sides does your dice have?")
    rolling = True
    while rolling:
        user_answer = input("Ready to Roll? Press ENTER to roll, or 'q' to quit")
        if user_answer.lower() != 'q':
            num_rolled = roll(int(sides))
            print("You rolled a ", num_rolled)
        else:
            rolling = False
    print("See ya!")

main()