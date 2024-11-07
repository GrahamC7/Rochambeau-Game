import random

# Define a dictionary to map numbers to choices and winning combos
choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
win_combos = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

# Welcome message
print("Welcome to Rochambeau! Get ready to throw down against the computer.")

# Game loop
while True:
  # Get user input
  while True:
    try:
      user_choice = int(input("Choose your weapon (1: Rock, 2: Paper, 3: Scissors, 0: Quit): "))
      if user_choice in range(1, 4) or user_choice == 0:
        break
      else:
        print("Invalid input. Please choose a number between 1 and 3.")
    except ValueError:
      print("Invalid input. Please enter a number.")

  # Quit if user chooses 0
  if user_choice == 0:
    break

  # Get computer's random choice
  computer_choice = random.randint(1, 3)

  # Print choices
  print(f"You chose: {choices[user_choice]}")
  print(f"Computer chose: {choices[computer_choice]}")

  # Determine winner
  if user_choice == computer_choice:
    print("It's a tie!")
  elif win_combos[choices[user_choice]] == choices[computer_choice]:
    print("You win!")
  else:
    print("Computer wins!")

  # Ask for another round
  play_again = input("Play again? (y/n): ")
  if play_again.lower() != "y":
    break

print("Thanks for playing!")
