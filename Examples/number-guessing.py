# -----------------------------
# Simple Number Guessing Game
# -----------------------------

secret = 9               # The secret number
guess_count = 0          # Number of guesses made
guess_limit = 3          # Maximum allowed guesses

print("Let's play a guessing game! You have 3 attempts to guess the number.")

while guess_count < guess_limit:
    guess = int(input("Guess a number: "))
    guess_count += 1
    
    if guess == secret:
        print("Congratulations! You guessed it right. You won!")
        break
    else:
        print("Wrong guess.")
        
else:
    # This block executes if the while loop completes without a break
    print("You lost! The secret number was", secret)