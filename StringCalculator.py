#Coding Challenge String Calculator
import re

#Part 1.
def add(numbers):
    #check that input is string
    if(isinstance(numbers, str)):
        #return 0 on empty string
        if(len(numbers)==0): 
            return 0        
        
        #replace all non-numeric characters with empty space
        #numbers = re.sub("[^0-9]", " ", numbers)
        numbers = re.sub(r'[^-\d]', " ", numbers)
        print("current string: " + numbers)

        #replace commas with spaces for list conversion
        numbers = numbers.replace(",", " ")

        #convert input to list of strings
        string_list = numbers.split()

        #convert list of strings into int map
        integer_map = map(int, string_list)
        #convert int map into int list
        integer_list = list(integer_map)
        return sum(integer_list)

    return ("Not a String")

#Test Cases
#part 1
"""
print("expected 0")
print(add(""))    
print("expected 3")
print(add("1,2"))


#part 2 any number of numbers 

print("expected 449")
print(add("4 6 55 5 3 34 342"))


#part 3 handle newlines \n

print("expected 9")
print(add("3\n3\n3"))
print("expected 6")
print(add("1\n2,3"))
print("expected 0")
print(add("\n"))


#part 4 handling any delimeter
    #solution - use regex to replace non-numbers with space 
print("expected 3")
print(add("//;\n1;2"))

""" 

#part 5 throw exception on negative numbers
print("expected 3")
print(add("//;\n1;2"))
print("expected negatives not allowed")
print(add("6, -4"))
