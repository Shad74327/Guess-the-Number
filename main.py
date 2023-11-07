from art import logo
import random
print(logo)

number = random.randint(0,101)

difficulty_level = input("Type 'hard' or 'easy'> ")

if difficulty_level == "hard":
    print("You have 5 attempts")
elif difficulty_level == "easy":
    print("You have 10 attempts.")

def result(attempt, number, guess):
    if attempt == 0:
        print(f"The number was {number}")
        print("You lose.")

    elif guess > number:
        print("Too High.")
        print(f"You have {attempt} attempts left.")

    elif guess < number:
        print("Too Low.")
        print(f"You have {attempt} attempts left.")

    elif guess == number:
        print("Congratulations! You win.")
        return True
        

if difficulty_level == "hard":

    x = 0
    while x<5:

        attempt = 4 - x
        guess = int(input("Guess the number: "))

        game_finished = result(attempt, number, guess) 
        
        if game_finished == True:
            break

        x+=1

if difficulty_level == "easy":

    x = 0
    while x < 10:

        attempt = 9 - x
        guess = int(input("Guess the number: "))

        game_finished = result(attempt, number, guess) 
        
        if game_finished == True:
            break
        x+=1