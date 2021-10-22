# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number 
# and for multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".
# If the number contains '7': Ding
# ------------------------------------------------------------------------
# I take what to "Ding" as a command prompt argument,
# maximum numbers range from the input
# Another improvement: It it consists of double digits print just "Double"

import sys
from test_class_print_numbers import Convertor_num_line

if (len(sys.argv) <= 1):
    print("An argument is expected! Exiting.")
    exit(1)
if (len(sys.argv[1]) != 1):
    print("Number from 0 to 9 as an argument is expected! Exiting.")
    exit(1)
else:
    what_to_ding = sys.argv[1]
# Input maximum range to iterate
#numbers_range = int(input("Please enter maximum number from 1 to 100: \n"))
#if ((numbers_range < 1) or (numbers_range > 100)):
#    print("Number form 1 to 100 is expexted! Exiting.")
#    exit(1)
numbers_range = 100
    
for index_number in range(1, numbers_range+1):
    print(f"{index_number}: {Convertor_num_line.num_to_line(index_number, what_to_ding)}")