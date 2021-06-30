import random

player_action = input("Coded by vNxr aka Nor, Enter a choice (rock, paper, scissors): ")
maybe_actions = ["rock", "paper", "scissors"]
AI_action = random.choice(maybe_actions)
print(f"\nYou chose {player_action}, AI chose {AI_action}.\n")

if player_action == AI_action:
    print(f"Each player chose {player_action}. It's specified as a tie!")
elif player_action == "rock":
    if AI_action == "scissors":
        print("Rock slams scissors! You gained a win!")
    else:
        print("Paper covers rock! You lost.")
elif player_action == "paper":
    if AI_action == "rock":
        print("Paper covers rock! You gained a win!")
    else:
        print("Scissors cuts paper! You lost.")
elif player_action == "scissors":
    if AI_action == "paper":
        print("Scissors slices paper! You gained a win!")
    else:
        print("Rock slams scissors! You lost.")
