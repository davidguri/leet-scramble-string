def toArray(string):
    array = []
    array[:0] = string
    return array
        
def checkArray(input_array, check_array):
    if set(input_array) == set(check_array):
        print(True)
    else:
        print(False)

string = input("Main string: ")
array = toArray(string)
check_string = input("Check string: ")
check_array = toArray(check_string)
checkArray(array, check_array)