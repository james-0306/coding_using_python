#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
# Ask the user to input 10 numbers
user_numbers = []
other_numbers = []
for i in range(10):
  input_number = int(input("Input number: "))
  user_numbers.append(input_number)
# Check the first number
for current_number in user_numbers:
    if current_number not in other_numbers:
        other_numbers.append(current_number)
#print the result
print(other_numbers)
