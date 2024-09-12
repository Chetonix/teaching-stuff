from hangman_art import stages, logo
from hangman_words import word_list
import random

print(logo)

random_word = random.choice(word_list)

display_list = []
for word in random_word:
    display_list += "_"


lives = 6

print(" ".join(display_list))

print(stages[lives])


while True:
    
    guess_letter = input("Enter a letter: ").strip().lower()


    if guess_letter in display_list:
        print("Chose Already!")
    elif guess_letter in random_word:
        for pos in range(len(random_word)):
            if random_word[pos] == guess_letter:
                display_list[pos] = guess_letter
    elif guess_letter not in random_word:
        print("Wrong Guess!")
        lives -= 1
        print(stages[lives])

    print(" ".join(display_list))

    if "_" not in display_list:
        print(f"You won!, the word was {random_word}")
        break

    if lives == 0:
        print(f"You lost! The word was {random_word}")
        break