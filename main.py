import random

def toArray(string):
    array = []
    array[:0] = string
    return array

def letter_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        print(arr[mid])
        if arr[mid] < int(x):
            low = mid + 1
        elif arr[mid] > int(x):
            high = mid - 1
        else:
            return mid
    return -1

def scrambleArr(array, length):
    if length == 0:
        print("Length = 0")
    else:
        scrambled = sorted(array, key = lambda x : random.random())
    return scrambled
        
def checkArray(input_array, check_array):
    for i in range(len(input_array)):
       result = letter_search(check_array, i)
       if result != -1:
            print(True)
       else:
            print(False)

string = "hello"
print("Main string: ", string)

array = toArray(string)
print("Main array: ", array)

len_array=len(array)
print("Len of array: ", len_array)

check_array = scrambleArr(array, len_array)
print("Check array: ", check_array)

len_check_array = len(check_array)
print("Len of check array: ", len_check_array)
checkArray(array, check_array)

