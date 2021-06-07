#Coding Challenge String Calculator

#Part 1.
def add(numbers):
    #check that input is string
    if(isinstance(numbers, str)):
        #return 0 on empty string
        if(len(numbers)==0): 
            return 0
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
print(add(""))    
print(add("1,2"))

#part 2 
print(add("4 6 55 5 3 34 342"))