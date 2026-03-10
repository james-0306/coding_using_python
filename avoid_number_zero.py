#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
# range the number to 0 to 100
for i in range(0, 101):
 # check if the number does not end to 0
 if i % 10 != 0:
     print(i)
#print the number