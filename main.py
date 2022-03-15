import random

# split two inputs into seperate arrays
# loop for each letter of unscrambled word if it is contained in the second array
# if all letters of first array are included, and the lenght of both arrays match then output true else false

def toArray(string):
    array = []
    array[:0] = string
    return array

def scrambleArr(array, length):
    if length == 0:
        print("Length = 0")
    else:
        scrambled = sorted(array, key = lambda x : random.random())
        print(scrambled)
        
def checkArray(input_array, check_array):
    for i in range(len(input_array)):
        if i in check_array:
            inArray = True
        else:
            inArray = False
    if inArray == True:
        print(inArray)
    else:
        print(False)
# this dont work, it broke

string = "hello"
array = toArray(string)
print(array)
scrambled_array = scrambleArr(array, len(array))
checkArray(array, scrambled_array)