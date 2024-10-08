import random

lowestnum = 1
maxnum = 100
win_num = random.choice(range(lowestnum, maxnum))

guesses = 1
max_guesses = 5
bonus = 1

print(f"Guess the number between {lowestnum} and {maxnum}. You have {max_guesses} guesses.")
while guesses <= max_guesses: 
    guess = int(input(
        f"[enter a # from {lowestnum}-{maxnum}]:"
    ))
    print(f"Your current guess is {guess}. You are  on guess # {guesses} of {max_guesses}")

    if guess > maxnum:
        print("Make sure to enter a number 1-25!")
        guesses -= 1
    elif guess <= 0:
        print("Make sure to enter a number 1-25!")
        guesses -= 1
    if abs(guess - win_num) <= 3:
        print("Your within 3! Here's an extra chance!")
        max_guesses += 1
    if guess == win_num:
        print("You win!")
        break
    guesses += 1
if guess != win_num:
        print("You lose! The correct number was", win_num)
    



