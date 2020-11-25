#Find the unique point in a list

def find_uniq(arr):
    res = arr[0] # Do XOR of all elements and returni    #range(1...) becayse res = arr[0]
    for i in range(1,len(arr)):  
        res = res ^ arr[i]
    
    return res #Floats are not supported with XOR operator

#Required no = 2*(sum_of_array_without_duplicates) - (sum_of_array)
#            = 2*(7 + 3 + 5 + 4) - (7 + 3 + 5 + 4 + 5 + 3 + 4) 
#            = 2*     19         -      31 
#            = 38 - 31
#            = 7 (required answer)


def single_number(arr):
    print(set(arr))    
    return 2 * sum(set(arr)) - sum(arr) 
















ar = [2, 20 , 3, 5, 4, 5, 3, 4]
arr =  [1, 1, 2, 1, 1 ]
print ("Element occurring once is", find_uniq(arr)) 
print ("Element occurring once is", single_number(arr)) 
print(ar[0])











