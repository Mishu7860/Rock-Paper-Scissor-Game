import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play a single round
def play_round():
    # User input
    user_choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()
    
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        return None, None

    # Computer's choice
    computer_choice = get_computer_choice()
    
    # Display choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    # Return result for score tracking
    if result == "You win!":
        return 1, 0
    elif result == "Computer wins!":
        return 0, 1
    else:
        return 0, 0

def main():
    user_score = 0
    computer_score = 0

    while True:
        # Play a round
        user_points, computer_points = play_round()
        
        # Update scores if a valid round was played
        if user_points is not None:
            user_score += user_points
            computer_score += computer_points

        # Display the score
        print(f"\nScore: You {user_score} - {computer_score} Computer")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()
