#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number
highest_number = None
# Make the user to input numbers
while True:
 user_input = (input("Enter a number: "))
# Make a program that break the loop
 if not user_input.isdigit():
  break
# covert str to int
 chosen_number = int(user_input)
if highest_number is None or chosen_number > highest_number:
    highest_number = chosen_number
print(highest_number)


