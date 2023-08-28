import art
import random
import replit

def guessing():
  def failed_attempt():
    if attempts > 0:
      return attempts - 1
    else:
      return attempts
    
  print(art.logo)

  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    print("You have 10 attempts remaining to guess the number")
    continue_guessing = True
    attempts = 10
    number = random.randint(0, 100)
    while continue_guessing is True:
      if attempts > 0:
        guess = int(input("Make a guess: "))
      if attempts == 0:
          continue_guessing = False
          print("Womp womp, you ran out of lives.")
      elif guess == number:
          continue_guessing = False
          print(f"Nice! You correctly guessed {number}")
      elif attempts > 0 and guess > number:
          print("Too high.")
          attempts = failed_attempt()
          print(f"You have {attempts} attempts left.")
          if attempts > 0:
            print("Guess again.")
      elif attempts > 0 and guess < number: 
          print("Too low")
          attempts = failed_attempt()
          print(f"You have {attempts} attempts left.")
          if attempts > 0:
            print("Guess again.")
      
  elif difficulty == "hard":
    print("You have 5 attempts remaining to guess the number.")
    continue_guessing = True
    attempts = 5
    number = random.randint(0, 100)
    while continue_guessing is True:
      if attempts > 0:
        guess = int(input("Make a guess: "))
      if attempts == 0:
          continue_guessing = False
          print("Womp womp, you ran out of lives.")
      elif guess == number:
          continue_guessing = False
          print(f"Nice! You correctly guessed {number}")
      elif attempts > 0 and guess > number:
          print("Too high.")
          attempts = failed_attempt()
          print(f"You have {attempts} attempts left.")
          if attempts > 0:
            print("Guess again.")
      elif attempts > 0 and guess < number: 
          print("Too low")
          attempts = failed_attempt()
          print(f"You have {attempts} attempts left.")
          if attempts > 0:
            print("Guess again.")
  else:
    print("I said 'easy' or 'hard'!")

  replay = input("Do you want to play another round? Type 'y' or 'n': ")
  if replay == "y": 
    replit.clear()
    guessing()
  else:
    print("Thanks for playing goober!")

guessing()
