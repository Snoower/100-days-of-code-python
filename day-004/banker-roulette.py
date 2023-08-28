import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

length = len(names)
random_choice = random.randint(0, length - 1)
random_person = names[random_choice]
print(f"{random_person} is going to buy the meal today!")
