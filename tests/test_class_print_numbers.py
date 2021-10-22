# Defining a class

"""Class to convert number to FizzBuzzDing string"""
class Convertor_num_line:
    def __init__(self) -> None:
        pass

#    def __init__(self, input_number: int) -> str:
#        self.input_class_number = input_number
    
    """Converter"""
    def num_to_line(number, num_to_ding):
        what_to_print = ""
        if ((number >=10) and (str(number)[0] == str(number)[1])):
            what_to_print = "Double"
        else:
            if (number % 3 == 0):
                what_to_print += "Fizz"
            if (number % 5 == 0):
                what_to_print += "Buzz"
            if (num_to_ding in str(number)): 
                what_to_print += "Ding"
            else:
                what_to_print = number     
        return what_to_print