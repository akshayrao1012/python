import random  # Import the random module to generate computer choices randomly

def get_user_choice():
    """Get user choice for rock, paper, or scissors."""
    user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()  # Prompt the user for their choice
    while user_choice not in ['rock', 'paper', 'scissors']:  # Validate user input
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    return user_choice

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])  # Randomly choose from rock, paper, or scissors for the computer

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"  # If user and computer choices are the same, it's a tie
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"  # User wins based on Rock-Paper-Scissors rules
    else:
        return "Computer wins!"  # Computer wins if none of the above conditions are met

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors Game!")

    while True:
        # Get user and computer choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        # Display choices
        print(f"\nYou chose {user_choice}.")
        print(f"Computer chose {computer_choice}.\n")

        # Determine and display the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Ask the user if they want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing Rock-Paper-Scissors!")
