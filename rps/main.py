from collections import Counter
import json
import random

def load_moves():
    try:
        with open("user_data.json", "r") as f:
            return json.load(f)
    except:
        return {"plays": []}

def save_moves(data):
    with open("user_data.json", "w") as f:
        json.dump(data, f, indent=2)

def computer_move(user_moves):
    if not user_moves:
        return random.choice(['rock', 'paper', 'scissors'])
    counts = Counter(user_moves)
    most_common = counts.most_common(1)[0][0]
    counter_moves = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
    return counter_moves[most_common]

def decide_winner(user, comp):
    if user == comp:
        return "Tie"
    if (user == 'rock' and comp == 'scissors') or \
       (user == 'paper' and comp == 'rock') or \
       (user == 'scissors' and comp == 'paper'):
        return "You win!"
    return "Computer wins!"

# Load data
user_data = load_moves()

while True:
    user_input = input("Rock, Paper or Scissors? (q to quit): ").lower()
    if user_input == 'q':
        print("Thanks for playing!")
        break
    if user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid input, try again.")
        continue

    user_data["plays"].append(user_input)
    comp = computer_move(user_data["plays"])
    print(f"Computer plays: {comp}")

    result = decide_winner(user_input, comp)
    print(result)

    save_moves(user_data)
