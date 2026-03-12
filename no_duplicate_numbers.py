#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
# Ask the user to input 10 numbers
user_number = []
for i in range(10):
    input_number = int(input(f"Input number{i+1}: "))
    user_number.append(input_number)
# print all the numbers that do not have duplicate
for current_number in user_number:
    if user_number.count(current_number) == 1:
        print(current_number)
