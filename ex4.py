
#
#You have an array of numbers.
#Your task is to sort ascending odd numbers but even numbers must be on their places.
#
#Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.
#



def sort_array(source_array):
    odd_numbers = sorted([n for n in source_array if n%2!=0])
    print(odd_numbers)
    c = 0
    res = []
    for i in source_array:
        if i %2!=0:
            res.append(odd_numbers[c])
            c += 1
        else:
            res.append(i)
    return res  



print(sort_array([2,3,1,2,6,8,7]))
