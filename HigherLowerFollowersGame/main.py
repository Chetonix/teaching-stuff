from art import vs, logo
from game_data import data
import random

print(logo)

account_a = random.choice(data)
account_b = random.choice(data)
while (account_a == account_b):
    account_b = random.choice(data)

def format_account(acc):
    return f"{acc['name']}, {acc['description']}, from {acc['country']}."

def is_correct(acc_a, acc_b, guess):
    if acc_a["follower_count"] > acc_b["follower_count"]:
        return guess == 'a'
    else:
        return guess == 'b'

score = 0

while True:
    print(format_account(account_a))
    print(vs)
    print(format_account(account_b))

    guess = input("Higher Followers: A or B: ").strip().lower()

    if is_correct(account_a, account_b, guess):
        score += 1
        print(f"Correct. Score: {score}")
        account_a = account_b
        account_b = random.choice(data)
        while (account_a == account_b):
            account_b = random.choice(data)
    
    else:
        print(f"That was wrong. Your score {score}.")
        break

else:
    print(f"You answered all of them correct. Score: {score}.")
