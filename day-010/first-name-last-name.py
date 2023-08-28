def format_name(first_name, last_name):
  """Take a first and last name and format it to return the title case version of the name."""
  if first_name == "" or last_name == "":
    return "You didn't provide valid inputs."
  else:
    formatted_f_name = first_name.title()
    formatted_l_name = last_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
