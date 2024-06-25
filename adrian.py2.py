from random import randint

def game_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif player_choice == "scissors" and computer_choice == "stone":
        return "Computer wins!"
    elif player_choice == "stone" and computer_choice == "scissors":
        return "Player wins!"
    else:
        return "Invalid input or rules not implemented for this case."

player_choice = input("Enter 'scissors' or 'stone': ").strip().lower()

# Check if the player's input is valid
while player_choice not in ['scissors', 'stone']:
    print("Invalid input. Please enter 'scissors' or 'stone'.")
    player_choice = input("Enter 'scissors' or 'stone': ").strip().lower()

# Generate computer's choice randomly
computer_choice = "scissors" if randint(1, 2) == 1 else "stone"

# Determine and print the result of the game
result = game_result(player_choice, computer_choice)
print(f"Player chose: {player_choice}")
print(f"Computer chose: {computer_choice}")
print(result)
