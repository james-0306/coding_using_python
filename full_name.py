#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

# Make the user to input their full name
full_name = input("Enter your full name: ")
# Remove the space at the beginning
space_name = full_name.lstrip()
print("The full name is: ", space_name)