#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
# ask the user to input number
number_set = []
for i in range(10):
    input_number = float(input("Enter the number: "))
    number_set.append(input_number)
# first number
result_number = number_set[0]
#subtract
for i in range(1, 10):
    result_number -= number_set[i]
#print
print(result_number)




