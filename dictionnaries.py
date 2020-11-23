

phonebooks = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

del phonebooks["John"]

phonebooks["Ticu"] = 40000000;


for name, number in phonebooks.items():
    print("Phone number of %s is %d" % (name,number))






