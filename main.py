#full credit to ChatGPT for this code cause I didnt have time to write this out
from js import alert, prompt, Math

def play_game():
    target = int(Math.floor(Math.random() * 100) + 1)
    attempts = 0
    alert("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    
    while True:
        guess_str = prompt("Enter your guess (1-100):")
        if guess_str is None:
            alert("Game cancelled.")
            break
        
        try:
            guess = int(guess_str)
        except ValueError:
            alert("That's not a number. Try again!")
            continue

        attempts += 1

        if guess < 1 or guess > 100:
            alert("Guess must be between 1 and 100.")
        elif guess < target:
            alert("Too low! Try again.")
        elif guess > target:
            alert("Too high! Try again.")
        else:
            alert(f"🎉 Correct! The number was {target}.\nYou guessed it in {attempts} tries.")
            break

play_game()
