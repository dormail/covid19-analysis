# function element_of(num,array) which checks if num is an element of array
def element_of(num, array):
    if len(array) == 0: # if array empty, num is no element of it
        return False
    
    if type(num) != type(array[0]): # TypeError when there are different datatypes
        raise TypeError
    
    for i in range(0,len(array)):
        if array[i] == num:
            return True
    
    return False
