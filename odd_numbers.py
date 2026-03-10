#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers
#Make an input program that allowed the users to input 10 numbers
total_number = 0
for i in range(10):
 number_set = float(input("Enter the a number: "))
# analyze the  numbers and print how many odd numbers
 if number_set % 2 != 0:
    total_number += 1
print("The total odd number is", total_number)

