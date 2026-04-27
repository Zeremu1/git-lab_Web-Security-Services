import random

def guess_the_number():
    """A simple number guessing game."""
    secret = random.randint(1, 100)
    attempts = 0
    
    print("🎯 Guess the number between 1 and 100!")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret:
                print("Too low! Try again.")
            elif guess > secret:
                print("Too high! Try again.")
            else:
                print(f"🎉 You got it in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
