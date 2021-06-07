#Coding Challenge - String Calculator
import re

#takes a string and returns sum of numbers within it,
# exception of negative numbers.
def add(numbers):
    #check that input is string
    if(isinstance(numbers, str)):
        #return 0 on empty string
        if(len(numbers)==0): 
            return 0        
        #replace all non-numeric characters with empty space
        numbers = re.sub(r'[^-\d]', " ", numbers)
        #convert input to list of strings
        string_list = numbers.split()
        #convert list of strings into int map
        integer_map = map(int, string_list)
        #convert int map into int list
        integer_list = list(integer_map)
        #adds negative ints found to error list
        neg_list = []
        for i in integer_list:
            if i < 0:
                neg_list.append(i)
        if(len(neg_list) > 0):
            negative_error = ValueError("Negatives not allowed ", neg_list)
            raise(negative_error)   
        #return sum of list if error not thrown
        return sum(integer_list)

    return ("Not a String")

#Test Cases
#part 1
"""
print("expected 0")
print(add(""))    
print("expected 3")
print(add("1,2"))
"""

#part 2 any number of numbers 
"""
print("expected 449")
print(add("4 6 55 5 3 34 342"))
"""

#part 3 handle newlines \n
"""
print("expected 9")
print(add("3\n3\n3"))
print("expected 6")
print(add("1\n2,3"))
print("expected 0")
print(add("\n"))
"""

#part 4 handling any delimeter
    #solution - use regex to replace non-numbers with space 
"""
print("expected 3")
print(add("//;\n1;2"))
"""
#part 5 throw exception on negative numbers
#print("expected 3")
#print(add("//;\n1;2"))
#print("expected ValueError: Negatives not allowed [-4]" )
#print(add("6, -4"))
print("expected ValueError: Negatives not allowed [-4, -7]" )
print(add("6, -4 sdggsg\n gwe totwe-7sdgwe"))


