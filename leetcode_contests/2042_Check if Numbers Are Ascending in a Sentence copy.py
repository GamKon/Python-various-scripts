# 2042. Check if Numbers Are Ascending in a Sentence
# A sentence is a list of tokens separated by a single space with no leading or trailing spaces. 
# Every token is either a positive number consisting of digits 0-9 with no leading zeros, 
# or a word consisting of lowercase English letters.
#
# For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens: "2" and "4" are numbers 
# and the other tokens such as "puppy" are words.
# 
# Given a string s representing a sentence, you need to check if 
# all the numbers in s are strictly increasing from left to right 
# (i.e., other than the last number, each number is strictly smaller than the number on its right in s).
#
# Return true if so, or false otherwise.
#
# class Solution:
#    def areNumbersAscending(self, s: str) -> bool:
#        for char in s:
#            print(char,"\n")
# tokens_string = input()

NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#list (range(10))
#print(NUMBERS)

def extract_numbers_list(s: str):
    numbers_list = [1]
    global NUMBERS
    number_str = ""
    s +=" "
    for input_char in s:
        if (input_char in NUMBERS):
            number_str += input_char
            #print("--",number_str)
        else:            
            try:
                number_int = int(number_str)
                number_str = ""
                if (number_int <= numbers_list[-1]):
                    return "FALSE \nNext number: "+str(number_int)+" isn't higher than previous "+ str(numbers_list[-1])+" !" 
                    #print("FALSE Next number is less than previous!")
                    exit(1)
                numbers_list.append(number_int)
                print(numbers_list)
            except ValueError:
                number_str = ""         
                # I know that except - pass is horrible for debugging and should be avoided in general.
                # But here it's a key element in the program's logic.
                # Random characters are passed to int() which should be just silently ignored
                pass
    #print("TRUE")  
    return "TRUE"    
        
tokens_string = "rr 2 33 777 r t 88"
#tokens_string = "hello world 5 x 5"
#tokens_string = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
#tokens_string = "4 5 11 26"
#tokens_string = "1 box has 3 blue 4 red 6 green and 12 yellow marbles 13 f"
print(extract_numbers_list(tokens_string))