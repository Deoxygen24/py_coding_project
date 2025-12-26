import random

number_to_guess = random.randint(1,100) # Generate a random number
trial_count = 0                         # Initiate trial_count
max_attempts = 4

while trial_count < max_attempts:
    try:
        user_guess = int(input('Guess a number between 1 and 100: '))
        if user_guess < number_to_guess:
            print("Your guess is too low")
        elif user_guess > number_to_guess:
            print("Your guess is too low")
        else:
            print("Congratulations, you guessed {number_to_guess} correctly !")
            break
    except ValueError:
        print('Please enter a valid number!')
    trial_count += 1                    # Increment trial count after each iteration

# If user have used up attempts and guess is incorrect
if trial_count == max_attempts and user_guess != number_to_guess:
    print(f"You've used up your {max_attempts} guess limit. The number is {number_to_guess}")