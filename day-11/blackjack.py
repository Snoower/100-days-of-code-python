import art
import replit
import random

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
replit.clear()

print(art.logo)

def blackjack():
  if start == "y": 
    
    continue_game = True    
    your_hand = []
    computer_hand = []

    for _ in range (2):
      your_hand.append(deal_card())
      computer_hand.append(deal_card())

    def calculate(card_sum):
      if sum(card_sum) == 21 and len(card_sum) == 2:
        return 0
      if 11 in card_sum and sum(card_sum) > 21:
        card_sum.remove(11)
        card_sum.append(1)
      return sum(card_sum)

    def compare(your_sum, computer_sum):
      if computer_sum == your_sum:
           return "Draw!"
      elif computer_sum == 0:
          return "Lose! Opponent has Blackjack!"
      elif your_sum == 0:
          return "Win! You have Blackjack!"
      elif computer_sum > 21:
          return "Opponent went over. You win!"
      elif your_sum > 21:
          return "You went over. You lose!"
      elif your_sum > computer_sum:
           return "You win!"
      else:
           return "You lose!"   
  
    while continue_game == True:
      your_sum = calculate(your_hand)
      computer_sum = calculate(computer_hand)
      print(f"  Your cards: {your_hand}, current score: {your_sum}")
      print(f"  Computer's first card: {computer_hand[0]}")
      
      if your_sum == 0:
        continue_game = False
      elif computer_sum == 0:
        continue_game = False
      elif your_sum > 21:
        continue_game = False
      else:
        new_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if new_card == "y": 
          your_hand.append(deal_card())
          your_sum = calculate(your_hand)
        else:    
          continue_game = False
        
    while computer_sum != 0 and computer_sum < 17:
      computer_hand.append(deal_card())
      computer_sum = calculate(computer_hand)  
     
    print(f"  Your final hand: {your_hand}, final score: {your_sum}")
    print(f"  Computer's final hand: {computer_hand}, final score: {computer_sum}")
    print(compare(your_sum, computer_sum))

  else:
      replit.clear()
      
  replay = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
  if replay == "y": 
    replit.clear()
    print(art.logo)
    blackjack()
  else:
    print("Thanks for playing!")
    
blackjack()
