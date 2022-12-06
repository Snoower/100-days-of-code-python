print("Welcome to the Tip Calculator!")

bill_total = input("What was the bill total? ")
bill_total_float = float(bill_total.replace('$', '')) #Bill Total

tip = input("What percentage would you like to tip? 10, 12, 15? ")
tip_as_int = int(tip)
tip_percentage = float((tip_as_int/100))
tip_total = bill_total_float*tip_percentage #Tip Total

total = bill_total_float+tip_total #Bill+Tip

people = input("How many people are splitting the bill? ")
people_int = int(people)
split = round(total/people_int,2)

print(f"Each person should pay: ${split}")
