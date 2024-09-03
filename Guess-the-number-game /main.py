import random

random_num = random.randint(1, 100)

attempts = 1

while True:

    try: 
        guess = int(input("Guess the number: "))
    except:
        print("Invalid input. Try again...")
        continue

    if guess == random_num:
        print(f"You guessed it right! The number was {random_num}.")
        print(f"You took {attempts} attempts to guess.")
        break

    elif guess > random_num:
        print("Guess lower!")
        attempts += 1

    elif guess < random_num:
        print("Guess Higher!")
        attempts += 1