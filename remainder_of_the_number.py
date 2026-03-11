#Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number
#Input 1
first_number = float(input("Enter the first number: "))
#Input 2
second_number = float(input("Enter the second number: "))
#analyze the remainder of the numbers
remainder_of_the_number = first_number % second_number
print('The remainder when the num',first_number, "is divided by", second_number, "is", remainder_of_the_number)