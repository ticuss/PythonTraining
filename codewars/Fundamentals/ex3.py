
def binary_array_to_number(arr):
        result = listToString(arr)

        return int(result,2)
   
def listToString(arr):
    str1 = ''
    for i in arr:
        str1 += str(i) 
    return str1






print(listToString([1,2,3]))
print(binary_array_to_number([0,0,1,1]))

