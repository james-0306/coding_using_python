#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function
sort_numbers = []

# Make the user to input number
while True:
   try:
    input_number = int(input("Enter a number: "))
    sort_numbers.append(input_number)
   except:
       break
# Use Sort program
sort_numbers.sort(reverse=True)
print("The Number from highest to lowest is: ", sort_numbers)

