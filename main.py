from replit import clear
import random
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculateScore(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score,computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if user_score == computer_score:
    return "Draw 🙃"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score>21:
    return "Opponent went over. You win 😁"
  elif computer_score==0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"
  

def play_game():
  print(logo)
  
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculateScore(user_cards)
    computer_score = calculateScore(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score >21:
      print("Hello")
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, Type 'n' to pass: ")
      if user_should_deal.lower() == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
    
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculateScore(computer_cards)

  print(f"Your final hand is {user_cards} and final score is {user_score}")
  print(f"Computer's final hand is {computer_cards} and final score is {computer_score}")
  print(compare(user_score,computer_score))

while input("Do you want to play the game of Blackjack? Type 'y' or 'n':").lower() == "y":
  clear()
  play_game()


