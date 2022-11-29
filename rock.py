import random 

while True:
    user_action = input("rock, paper or scissor? ")
    possible_actions = ["rock", "paper", "scissor"]
    computer_action = random.choice(possible_actions)

    while user_action not in ("rock", "paper", "scissor"):
        print("spell it right to play")
        user_action = input("rock, paper or scissor? ")

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action: 
        print("TIE")
    elif user_action == "rock":
        if computer_action == "scissor":
            print("WINNER")
        else: 
            print("LOSER")
    elif user_action == "scissor":
        if computer_action == "paper":
            print("WINNER")
        else: 
            print("LOSER")
    elif user_action == "paper":
        if computer_action == "rock":
            print("WINNER")
        else: 
            print("LOSER")

    play_again = input ("play again? y/n: ")
    if play_again != "y":
        break

