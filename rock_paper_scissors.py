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

import random
print("Welcome to the Rock, Paper, Scissors game!")
user_choice= int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
computer_choice_random = random.randint(0, 2)
if user_choice == 0:
    print('you choose rock')
    print(rock)
    if computer_choice_random == 0:
        print('computer choose rock')
        print(rock)
        print('it is a draw')
        if computer_choice_random == 1:
            print('computer choose paper')
            print(paper)
            print('you lose')
            if computer_choice_random == 2:
                print('computer choose scissors')
                print(scissors)
                print('you won')
elif user_choice == 1:
    print("you choose paper")
    print(paper)
    if computer_choice_random == 0:
        print('computer choose rock')
        print(rock)
        print('you lose')
        if computer_choice_random == 1:
            print('computer choose paper')
            print(paper)
            print('it is a draw')
            if computer_choice_random == 2:
                print('computer choose scissors')
                print(scissors)
                print('you lose')
elif user_choice == 2:
    print('you choose scissors')
    print(scissors)
    if computer_choice_random == 0:
        print('computer choose rock')
        print(rock)
        print('you lose')
        if computer_choice_random == 1:
            print('computer choose paper')
            print(paper)
            print('you win')
            if computer_choice_random == 2:
                print('computer choose scissors')
                print(scissors)
                print('it is a draw')