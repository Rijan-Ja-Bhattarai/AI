import json

# Load and Save Functions
def load_moves(filename="user_data.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"plays": []}  # default data

def save_moves(data, filename="user_data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

# Load previous data
user_history = load_moves()

# Game loop
while True:
    user_input = input("Rock, Paper, or Scissors? (q to quit): ").lower()

    if user_input == 'q':
        print("Thank you for playing!")
        break

    if user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Try again.")
        continue

    # Append valid input to history
    user_history["plays"].append(user_input)

    # Save updated data
    save_moves(user_history)
