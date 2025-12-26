import random

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'
emojis = {'r': '🪨', 'p': '📄', 's':'✂️'}
choices = tuple(emojis.keys())     # Tuple is Read only

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper, or Scissor? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice !')
        
def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(f'Tie!')
    elif(
        (user_choice == ROCK and computer_choice == SCISSOR) or
        (user_choice == SCISSOR and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)): 
        print(f'You win')
    else:
        print('You lose')
        
def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)

        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break

play_game()
        
        

        
