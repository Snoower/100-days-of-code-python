from replit import clear
import random
import hangman_words #could also do from hangman_words import word_list

chosen_word = random.choice(hangman_words.word_list) 
word_length = len(chosen_word)

end_of_game = False
lives = 6

import hangman_art #could also do from hangman_art import logo, stages
print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
  
    clear()
  
    if guess in display:
      print(f"You already guessed {guess}.")
      
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word! You lose a life.")
        if lives == 0:
            end_of_game = True
            print(f"You lose, the word was {chosen_word}.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
