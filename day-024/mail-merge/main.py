with open("Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()

with open("Input/Names/invited_names.txt") as name_list:
    name_contents = name_list.readlines()
    for name in name_contents:
        stripped_name = name.strip("\n")
        replace_name = letter_contents.replace("[name]", stripped_name)
        output_directory = "Output/ReadyToSend/"
        with open(f"{output_directory}letter_for_{stripped_name}", mode='w') as completed_letter:
            completed_letter.write(replace_name)
