import art
import game_data
import random
from replit import clear

previous_option_b = ""
has_won = False
has_lost = False
score = 0

def run_game():
  # Imports global variables into the function
  
  global previous_option_b
  global has_won
  global has_lost
  global score

  # Clears the console and prints the logo
  clear()
  print(art.logo)

  # Prints the user's score if the user has won the previous round
  if has_won == True:
    print(f"You are correct. You have a score of {score}")

  # Checks if the user has not lost the previous round. Will end the function if has_lost is equal to true
  if not has_lost:
    if previous_option_b == "":
      option_a = random.choice(game_data.data)
    else:
      option_a = previous_option_b

    # Assigns the values of the option_a dictionary into local variables
    option_a_name = option_a['name']
    option_a_followers = option_a['follower_count']
    option_a_description = option_a['description']
    option_a_country = option_a['country']

    # Picks  a random dictionary for option_b
    option_b = random.choice(game_data.data)

    # Prevents option_b from being the same thing as option_a
    while option_b == option_a:
      option_b = random.choice(game_data.data)

    # Puts everything from the dictionary of option_b into local variable
    
    option_b_name = option_b['name']
    option_b_followers = option_b['follower_count']
    option_b_description = option_b['description']
    option_b_country = option_b['country']

    # Prints option_a, the VS ascii art, and option_b in this order
    print(f"Option A: {option_a_name}, a {option_a_description} from {option_a_country}")
    print(art.vs)
    print(f"Option B: {option_b_name}, a {option_b_description} from {option_b_country}")

    # Takes the user's input and assigns it to user_answer
    user_answer = input("Who has more followers? Enter 'a' or 'b'. ").lower()

    # Determines who has more followers between option_a and option_b
    
    winner = ""
    if option_a_followers > option_b_followers:
      winner = option_a
    else:
      winner = option_b

    # Sets the previous option b variable to the current option b. This variable will be used to set option A to the previous option B
    previous_option_b = option_b
  
    # Checks if the user has pick the right optioned and edits global variables like score depending on the outcomes
    if (winner == option_a and user_answer == "a") or (winner == option_b and user_answer == "b"):
      score += 1
      has_won = True
    else:
      has_won = False
      has_lost = True

    # Recursion
    run_game()




  else:
    # Prints the final score
    print(f"Sorry, that was incorrect. Score: {score}")

# Code starts here. First thing to be run.

run_game()