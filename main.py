from art import logo
import random
print(logo)

number = random.randint(0,101)

difficulty_level = input("Type 'hard' or 'easy'> ")

if difficulty_level == "hard":
    """ Difficulty level Hard """

    for x in range(5):
        """ Here total 5 attempts available """

        attempt = 4 - x
        guess = int(input("Guess the number: "))

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
            break
        

if difficulty_level == "easy":
    """ Difficulty level easy """

    for x in range(10):
        """ Here total 10 attempts available """

        attempt = 9 - x
        guess = int(input("Guess the number: "))

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
            break
        