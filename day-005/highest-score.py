student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max = 0
for highest_number in student_scores:
  if highest_number > max:
    max = highest_number
print(f'The highest score in the class is: {max}')
