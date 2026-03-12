#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
# Input 1
num_list = []
first_number = int(input("First number: "))
# Input 2
second_number = int(input("Second number: "))
# make a range
for i in range(first_number + 1, second_number):
    num_list.append(i)
#print the numbers between
num_set = [print(i, end=",") for i in num_list]
