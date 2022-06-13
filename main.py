import random
print("Rock , Paper, Scissors Game")

is_running = True

while is_running:
    player_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ['rock', 'paper', 'scissors']
    computer_action = random.choice(possible_actions)
    print(f"\n Player {player_action} : CPU {computer_action}.\n")

# looping player vs compurter possible choices

    if player_action == computer_action:
        print(f"Both players selected {player_action}. It's a draw!")
    elif player_action == 'rock':
        if computer_action == 'scissors':
            print("Rock beats scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player_action == 'paper':
        if computer_action == 'rock':
            print("Paper beats rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player_action == 'scissors':
        if computer_action == 'paper':
            print("Scissors beats paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    else:
        # Invalid operation
        print("Invalid choice entered, try again...")

    choice = input("Would you play again. [y,n] :")
    if choice == "y":
        pass

    if choice == "n":
        is_running = False
        print('thanks for playing. bye')
