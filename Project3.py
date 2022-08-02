import random
import math
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
type = input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.\n")
computer = str((random.randint(0,2)))
if type=='0':
    print(rock)
    print("Computer chose:")
    if computer=='2':
       print(scissors)
       print("You Win")
    elif computer=='1':
        print(paper)
        print("You Loose")
    else:
        print(rock)
        print("It's a Draw")
if type=='1':
    print(paper)
    print("Computer chose:")
    if computer=='0':
       print(rock)
       print("You Win")
    elif computer=='2':
        print(scissors)
        print("You Loose")
    else:
        print(paper)
        print("It's a Draw")
if type=='2':
    print(scissors)
    print("Computer chose:")
    if computer=='1':
       print(paper)
       print("You Win")
    elif computer=='0':
        print(rock)
        print("You Loose")
    else:
        print(scissors)
        print("It's a Draw")
else:
    print("You Loose!!!")

