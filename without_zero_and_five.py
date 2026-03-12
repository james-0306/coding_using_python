#Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
# make a range from 0 to 100
for i in range(0, 101):
# remove all the zero's and five's and print
 if i % 5!= 0 and i % 10 != 0:
     print(i)
