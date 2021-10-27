# 2027. Minimum Moves to Convert String
# You are given a string s consisting of n characters which are either 'X' or 'O'.
# A move is defined as selecting three consecutive characters of s and converting them to 'O'. 
# Note that if a move is applied to the character 'O', it will stay the same.
# Return the minimum number of moves required so that all the characters of s are converted to 'O'
#
# class Solution:
#     def minimumMoves(self, s: str) -> int:
        

def replace_and_count (string_for_replacement: str):
    count_replacements = 0    
    
    while "XXX" in string_for_replacement:
        string_for_replacement = string_for_replacement.replace("XXX", "OOO", 1)
        print(string_for_replacement)
        count_replacements += 1
    while "XX" in string_for_replacement:
        string_for_replacement = string_for_replacement.replace("XX", "OO", 1)
        print(string_for_replacement)
        count_replacements += 1
    while "XOX" in string_for_replacement:
        string_for_replacement = string_for_replacement.replace("XOX", "OOO", 1)
        print(string_for_replacement)
        count_replacements += 1    
    while "X" in string_for_replacement:
        string_for_replacement = string_for_replacement.replace("X", "O", 1)
        print(string_for_replacement)
        count_replacements += 1
                  
    return count_replacements


#given_string = "XXXOOOXXOXOOOOXXXOXOX"
given_string = "XXXOXOXXXX"
#given_string = "OOOO"
print(f"\n{given_string}\nMinimum iterations to replace XXX to OOO:\n{replace_and_count(given_string)}")


