import random
import art

from replit import clear

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

card_names = {
     cards[0]: "Ace",
     cards[1]: "Two",
     cards[2]: "Three",
     cards[3]: "Four",
     cards[4]: "Five",
     cards[5]: "Six",
     cards[6]: "Seven",
     cards[7]: "Eight",
     cards[8]: "Nine",
     cards[9]: "Ten",
     cards[10]: "Jack",
     cards[11]: "Queen",
     cards[12]: "King"
}

def run_blackjack():
  user_hand = []
  computer_hand = []
  clear()
  print(art.logo)
  deal(user_hand, 2)
  user_score = calculate_score(user_hand)
  
  print("Your hand: " + print_hand(user_hand))
  print("This hand has a score of " + str(user_score) + "\n")
  
  deal(computer_hand, 2)
  computer_score = calculate_score(computer_hand)

  print("Right now, the computer's hand is: [" + card_names[computer_hand[0]] + ", ?]\n")
  user_hit_input = input("Do you wish to hit or stand? 'y' for hit, 'n' for stand\n")

  while user_hit_input == "y" and user_score <= 21:
    deal(user_hand, 1)
    user_score = calculate_score(user_hand)
    print("Your hand is now " + print_hand(user_hand))
    print("This hand has a score of " + str(user_score))
    user_hit_input = input("Do you want to hit again?\n")


  print("Computer's hand: " + print_hand(computer_hand))
  print("It has a score of " + str(computer_score) + "\n")

  
  find_winner(user_score, computer_score)

  
  user_restart_input = input("Do you want to play again? 'y' for yes, 'n' for no\n")
  if user_restart_input == "y":
    run_blackjack()
  
  

def deal(hand, times):
  for i in range(times):
    hand.append(random.choice(cards))

def calculate_score(hand):
  score = 0
  for points in hand:
    if points == 11 and score > 21:
      score += 1
    else:
      score += points
  return score

def find_winner(score_1, score_2):
  if score_1 <= 21 and score_2 <= 21:
    if score_1 > score_2:
      print("User wins!!!")
    elif score_1 < score_2:
      print("Computer wins!!!")
    else:
      print("Draw!!!")
  else:
    if score_1 > 21:
      print("Computer wins!!!")
    else:
      print("User wins!!!")

def print_hand(hand):
  deck_str = "["
  for index in range(len(hand)):
    deck_str += card_names[hand[index]]
    if index != (len(hand) - 1):
      deck_str += ", "

  deck_str += "]"
  return deck_str

# Code starts here when run

user_input = input("Do you want to play Blackjack? Enter 'y' or 'n'\n")

if user_input == "y":
  run_blackjack()
