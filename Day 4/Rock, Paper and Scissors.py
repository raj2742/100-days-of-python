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
list_item=[rock,paper,scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(list_item[user_input])
computer_input=random.randint(0,2)
print(f"Computer input: {computer_input}")
print(list_item[computer_input])

if user_input<0 and user_input>2:
    print("Game Over. Enter the Valid Choice")
elif user_input == 2 and computer_input == 0:
    print("You Win.")
elif user_input == 0 and computer_input == 2:
    print("You Lose.")
elif computer_input > user_input:
    print("You Lose.")
elif user_input > computer_input:
    print("You Win.")
elif user_input == computer_input:
    print("The Match is draw.")
