


    
def positive_sum(arr):
    ans= 0
    for i in arr:
        if i > 0:
            ans = ans + i
    return ans
        

arr = []            
arr = [5,2,3,4,5]    
an = positive_sum(arr)
print(an)




