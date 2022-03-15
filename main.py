import random

# split two inputs into seperate arrays
# loop for each letter of unscrambled word if it is contained in the second array
# if all letters of first array are included, and the lenght of both arrays match then output true else false

def toArray(string):
    array = []
    array[:0] = string
    return array

def scrambleStr(array, length):
    if length == 0:
        print("Length = 0")
    else:
        scramble_array = random.shuffle(array)
        print("Scramble array>>>")
        print(scramble_array)
        
        
string = "hello"
array = toArray(string)
print("Scramble string")
print(scrambleStr(toArray(string), len(string)))