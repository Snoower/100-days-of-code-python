from replit import clear
from art import logo

bids = {}
continue_bid = True

def add_new_bid(bidder_name, bidder_bid):
  bids[bidder_name] = bidder_bid
  
while continue_bid == True:
  print(logo)
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  add_new_bid(bidder_name=name, bidder_bid=bid)
  decision = input("Are there any other bidders? Type 'yes' or 'no' \n")
  
  if decision == "yes":
     clear()  
  if decision == "no":
    continue_bid = False
    winner_name = max(bids, key=bids.get)
    winner_bid = max(bids.values())
    print(f"The winner is {winner_name} with a bid of ${winner_bid}!")
