#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
number_set =[]
# Make the user Input numbers
while True:
    try:
        input_number = int(input("Enter a number: "))
        number_set.append(input_number)
    except:
        break
# Compute the average
average_number = sum(number_set) / len(number_set)
print("The average is: ", average_number)