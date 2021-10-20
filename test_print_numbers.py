# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number 
# and for multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".
# If the number contains '7': Ding
# ------------------------------------------------------------------------
# I take what to "Ding" as a command prompt argument
# Maximum numbers range from the input
# Another improvement: It it consist of double digits print just "Double"

import sys

if (len(sys.argv[1]) != 1):
    print("Number from 0 to 9 as an argument expected! Exiting.")
    exit(1)

numbers_range = int(input("What is the numbers range? \n"))
    
for number in range(1, numbers_range+1):
    what_to_print = ""
    if ((number >=10) and (str(number)[0] == str(number)[1])):
        what_to_print = "Double"
    else:
        if (number % 3 == 0):
            what_to_print += "Fizz"
        if (number % 5 == 0):
            what_to_print += "Buzz"
        if (sys.argv[1] in str(number)): 
            what_to_print += "Ding"
        if (what_to_print.__len__ == 0):
            what_to_print = number    
    print(number,":",what_to_print)