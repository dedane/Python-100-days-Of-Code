import random

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

selection = input('What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors: ')
your_selection = int(selection)

random_selection = random.randint(0,2)
computer = random_selection

if your_selection == 0:
    print(rock)
    if computer == 1:
        print(f'computer choose:{paper}, You have lost')
    elif computer == 0:
        print(f'computer choose:{rock}, Its a draw')
    elif computer == 2:
        print(f'Computer choose: {scissors}, You Win')
elif your_selection == 1:
    print(f'you choose:{paper}' )
    if computer == 1:
        print(f'computer choose:{paper}, its a draw')
    elif computer == 0:
        print(f'computer choose:{rock}, You have Won')
    elif computer == 2:
        print(f'Computer choose: {scissors}, You have lost')
elif your_selection == 2:
    print(scissors)
    if computer == 1:
        print(f'computer choose:{paper}, You have Won')
    elif computer == 0:
        print(f'computer choose:{rock}, You have lost')
    elif computer == 2:
        print(f'Computer choose: {scissors}, its a draw')

else:
    print('Your selection is not valid')