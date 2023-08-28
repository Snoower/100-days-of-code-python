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

choices = [rock, paper, scissors]

person_choice = int(input("Make your choice! Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if person_choice == 0:
    print(f"{rock}")
elif person_choice == 1:
    print(f"{paper}")
elif person_choice == 2:
    print(f"{scissors}")

length = len(choices)
random_choice = random.randint(0, length - 1)
computer_choice = choices[random_choice]
if person_choice <= 2:
    print(f"Computer chose:\n {computer_choice}")
else:
    print("I SAID 0, 1, OR 2! (ノ°Д°）ノ︵ ")

if computer_choice == choices[0] and person_choice == 0:
    print("It's a draw.")
elif computer_choice == choices[1] and person_choice == 0:
    print("You lose!")
elif computer_choice == choices[2] and person_choice == 0:
    print("You win!")
  
if computer_choice == choices[1] and person_choice == 1:
    print("It's a draw.")
elif computer_choice == choices[2] and person_choice == 1:
    print("You lose!")
elif computer_choice == choices[0] and person_choice == 1:
    print("You win!")
  
if computer_choice == choices[2] and person_choice == 2:
    print("It's a draw.")
elif computer_choice == choices[0] and person_choice == 2:
    print("You lose!")
elif computer_choice == choices[1] and person_choice == 2:
    print("You win!")
