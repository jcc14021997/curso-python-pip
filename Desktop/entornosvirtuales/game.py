import random

'''list_option = ('stone', 'scissors', 'paper')


cont_user = 0
cont_computer = 0

while cont_user < 4 or cont_computer < 4:
    user_computer = random.choice(list_option)
    user= input('stone, scissors, paper => ').lower()

    
    if not user in list_option:
        print('OPTION INVALID!!!!!')
        continue


    if user_computer == user:
        print('TIE!')
    elif (user_computer == 'stone' and user == 'scissors') or (user_computer == 'scissors' and user == 'paper') or (user_computer == 'paper' and user == 'stone'):
        print('USER_COMPUTER WINNER')
        cont_computer += 1
        print('COUNT USER_COMPUTER: ',cont_computer)
        print('COUNT USER: ',cont_user)
    else:
        print('USER WINNER')
        cont_user += 1
        print('COUNT USER', cont_user)
        print('COUNT USER_COMPUTER', cont_computer)

    print('OPTION USER COMPUTER: ', user_computer )'''
# Define the list of possible options
list_options = ["stone", "scissors", "paper"]

# Initialize counters
user_wins = 0
computer_wins = 0

while user_wins < 3 and computer_wins < 3:
    # Generate computer's choice randomly
    computer_choice = random.choice(list_options)

    # Get user input and ensure it's valid
    user_choice = input("stone, scissors, paper => ").lower()
    if user_choice not in list_options:
        print("Invalid option! Choose from:", ", ".join(list_options))
        continue

    # Compare choices and update counters
    if user_choice == computer_choice:
        print("Tie!")
    elif (user_choice == "stone" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "stone"):
        print("You win!")
        print('Option computer: ' + computer_choice)
        user_wins += 1
        print('USER ' ,user_wins)
        print('COMPUTER ' ,computer_wins)
    else:
        print("Computer wins!")
        print('Option computer: ' + computer_choice)
        computer_wins += 1
        print('USER ' ,user_wins)
        print('COMPUTER ' ,computer_wins)

# Print final scores
print("Final score:")
print("You:", user_wins)
print("Computer:", computer_wins)
