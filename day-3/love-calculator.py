print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

truecount = 0 #easier method would have been t = lower_case_string.count("t") etc then true = t + r + u + e
for i in lower_name1:
    if i == "t":
        truecount += 1
    if i == "r":
        truecount += 1
    if i == "u":
        truecount += 1
    if i == "e":
        truecount += 1
for i in lower_name2:
    if i == "t":
        truecount += 1
    if i == "r":
        truecount += 1
    if i == "u":
        truecount += 1
    if i == "e":
        truecount += 1

lovecount = 0 #easier method would have been l = lower_case_string.count("l") etc then love = l + o + v + e
for i in lower_name1:
    if i == "l":
        lovecount += 1
    if i == "o":
        lovecount += 1
    if i == "v":
        lovecount += 1
    if i == "e":
        lovecount += 1
for i in lower_name2:
    if i == "l":
        lovecount += 1
    if i == "o":
        lovecount += 1
    if i == "v":
        lovecount += 1
    if i == "e":
        lovecount += 1

score = int(str(truecount) + str(lovecount)) # lovescore = love + true

if score > 90 or score < 10:
    print(f"Your score is {score}, you go together like coke and mentos. ")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together. ")
else:
    print(f"Your score is {score}. ")


