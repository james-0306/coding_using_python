#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
# Make an Input program to ask the user to input numbers
input_number = input("Enter a Number: ")
#Print the result with 6 digits
print(input_number.zfill(6))