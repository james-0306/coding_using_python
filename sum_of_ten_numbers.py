#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
#Make an input program to allowed users to input a numbers
total_sum = 0
for i in range(10):
    number_set = float(input("Enter the a number: "))
 # sum all the numbers and print the answer
    total_sum += number_set
print(total_sum)


