import random

# split two inputs into seperate arrays
# loop for each letter of unscrambled word if it is contained in the second array
# if all letters of first array are included, and the lenght of both arrays match then output true else false

def toArray(string):
    array = []
    array[:0] = string
    return array

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def scrambleArr(array, length):
    if length == 0:
        print("Length = 0")
    else:
        scrambled = sorted(array, key = lambda x : random.random())
        print(scrambled)
        
def checkArray(input_array, check_array):
    for i in range(len(input_array)):
       binary_search(check_array, i)
       if result != -1:
            print(True)
       else:
            print(False)
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
