import random
# Print random from list/tuple
# ask user to guess (r/p/s)
# u.Rock + c.Paper = lose
# u.Paper + c.Rock = lose
# u.Scissor + c.Rock = lose

# u.rock + c.scissor = win
# u.Scissor + c.Paper = win
# userinput is  invalid: print err
#    if user choose ✂️ and computer 📄 or 🪨 and choose ✂️
#       usr win
#    else
#        user lose
emojis = {'r': '🪨', 'p': '📄', 's':'✂️'}
choices = ('r','p','s')     # Tuple is Read only

# print(computer_choice)
while True:
        user_choice = input("Rock, Paper, or Scissor? (r/p/s): ").lower()
        if user_choice not in choices:
            print('Invalid choice!')
            continue
        computer_choice = random.choice(choices)
        print(f'You chose {emojis[user_choice]}')
        print(f'Computer chose {emojis[computer_choice]}')

        if user_choice == computer_choice:
             print(f'Tie!')
        elif(
            (user_choice == 's' and computer_choice == 'p') or
            (user_choice == 'r' and computer_choice == 's') or
            (user_choice == 'p' and computer_choice == 's')): 
            print(f'You win')
        else:
           print('You lose')
        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break
