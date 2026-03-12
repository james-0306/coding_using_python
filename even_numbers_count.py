#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
#input numbers
even_numbers = 0
for i in range (10):
 number_set = int(input(f"Enter a number {i+1}:"))
# check how many even numbers
 if number_set % 2 == 0:
  even_numbers += 1
#print how many even numbers
print(even_numbers)