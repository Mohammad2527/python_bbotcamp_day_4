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

game_image = [rock, paper, scissors]
# Selecting rock, paper or scissors
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor\n"))
if (my_choice > 2) or (my_choice < 0):
    print("You entered an invalid number, you lose!")
else:
    print(game_image[my_choice])
# Generating random number between 0 and 2 for the computer to choose rock, paper or scissors
    computer_choice = random.randrange(0,3)
    print("Computer chose:")
    print(game_image[computer_choice])
    
    if (my_choice == computer_choice):
        print("It's a draw")
    elif (my_choice == 0):
        if (computer_choice == 1):
            print("You lose!")
        else:
            print("You win!")
    elif (my_choice == 1):
        if(computer_choice == 0):
            print("You win!")
        else:
            print("You lose!")
    elif (my_choice == 2):
        if (computer_choice == 1):
            print("You win!")
        else:
            print("You lose!")


    
