#Convert number to reversed array of digits
#Given a random non-negative number, you have to return the digits of this number within an array in reverse order.Given a random non-negative number, you have to return the digits of this number within an array in reverse order.Given a random non-negative number, you have to return the digits of this number within an array in reverse order.


def digitize(n):
    liste = []
    listenew = []
    new = str(n)
    for i in new: 
        liste += i
        print(liste)
    listenew =  liste[::-1] 
    return reverse(listenew)


def reverse(test_list):
    test_list = [int(i) for i in test_list] 
    return test_list





print(digitize(35231))








