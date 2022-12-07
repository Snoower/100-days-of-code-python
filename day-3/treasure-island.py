print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n") 

direction = input("You find yourself at a crosspaths. Do you want to go left, where you see something sparkling? Or would you like to go right towards the sea? ").lower()

if direction == "left":
  ride = input('You come across a man named Rick that is setting up his shoddily-built raft. "Need a *burp* ride?" Y or N. ').lower()
  if ride == "y":
    print("You accept this man's kind offer. You two get to chatting it up, when a thought comes across your mind, 'Wow, what a cool guy. Maybe I'll ask him to accompany me on my quest for this trea--'. Your thought is cut short when a Cronenbergian monster comes out of the water and eats you both. You died. Game Over.")
  else:
    door = input('You kindly decline his offer. He responds, "ipso fuckoffo" as he sails away, his middle finger high up in the air. You start walking off in the other direction, where you come across a strange house. You walk in to find three coloured doors. One is red, one is blue, and the other is green. Which door do you choose to open? ').lower()
    if door == "red":
      print("You got spooked by Scary Terry and died. Game Over.")
    elif door == "blue":
      print("You tripped into a green portal, got shredded, and died. Game Over.")
    elif door == "green": 
      print('Congrats! You found the treasure. Its a Mr. Meeseeks box. You push the button and out comes a Meeseeks that says, "IM MR. MEESEEKS LOOK AT ME!" ')
    else:
      print("You vaporize where you stand. You died. Game Over.")
else:
  print("Excitingly, you sprint towards what you believe is the treasure. Unfortunately, you tripped on a rock and died. Game Over.")
