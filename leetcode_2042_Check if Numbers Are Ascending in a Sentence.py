NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#list (range(10))
print(NUMBERS)

def extract_numbers_list(s: str):
    numbers_list = [0]
    global NUMBERS
    number_str = ""
    s +=" "
    for index in range(len(s)):
        input_char = s[index]
        if (input_char in NUMBERS):
            number_str += input_char
            #print("--",number_str)
        else:            
            try:
                number_int = int(number_str)
                number_str = ""
                if (number_int <= numbers_list[-1]):
                    print("Next number is less than previous!")
                    exit(1)
                numbers_list.append(number_int)
                print(numbers_list)
            except Exception: 
                number_str = ""         
                pass
      
        
        
#tokens_string = "1 2 33 777 r t 888"
tokens_string = "1 box has 3 blue 4 red 6 green and 12 yellow marbles 1"
extract_numbers_list(tokens_string)