#ROT13 is a simple letter substitution cipher that
#replaces a letter with the letter 13 letters after
#it in the alphabet. ROT13 is an example of the Caesar cipher.

#Create a function that takes a string and returns the stringi
#ciphered with Rot13. If there are numbers or special characters
#included in the string, they should be returned as they are. Only 
#letters from the latin/english alphabet should be shifted, like in
#the original Rot13 "implementation".

def rot13(s):
    from codecs import encode
    return encode(s, 'rot13')

def rot133(message):
    return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))



print("",rot133('blaaaablaaaa'))
