


###########PYTHON BASICS#############

print("------------EXERCICE  1-------------")
print("hello world");
print("hello world");

x = 1
if x == 1: 
    print ("x = 1 "); 
########EXERCICE2########### 

print("------------EXERCICE  2-------------")
myfloat = 7.0
print (myfloat)    
myfloat = float(75);
print(myfloat); 



########EXERCICE3########### 

print("------------EXERCICE  3-------------")
hello = 'hello'
world = "world"
helloworld = hello +" " + world 
print(helloworld); 


########EXERCICE4########### 

print("------------EXERCICE  4-------------")
mylist = [10,15,12];
mylist.append(10);
mylist.append(11);
mylist.append(12);
mylist.append(13);
mylist.append(14);
mylist.append(15);
for x in mylist: 
    print(x);



########EXERCICE5########### 
print("------------EXERCICE  5-------------")
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)



########EXERCICE6########### 
print("------------EXERCICE  6-------------")
print("\n")
print("Arithmetics");

number = 1+2*3/4.0
squared = 7**2
cube = 2**3
print(number);
print(squared);
print(cube);

print("\n")
lotofhello = "\n hello" * 20 
print(lotofhello)

print("\n")
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print("Addition of 2 lists",all_numbers)
print("List * 3",[1,2,3] * 3)


print("\n")
########EXERCICE7########### 

print("\n")
print("------------EXERCICE  7-------------")
print("STRING FORMATTING")
name = "John"
print("Hello, %s!" %name);

age = 23 

print("%s is %d years old." %(name, age))

mytlist = [1,2,3]
print('A list :%s' % mylist)
data = ("John", "Doe", 53.44)
print("%s %s %d"   % data)


print("\n")



########EXERCICE8########### 

print("\n")

print("------------EXERCICE  8-------------")
print("ceva"); 
print("STRING OPERATIONS")

astring = "Hello World"

print(" len() = size of the string",len(astring))
print("")
print("string.index(Letter of the string) = ", astring.index("o"))
print("\n")
print("String from[3:7]==", astring[3:7])
print("\n")
print("string.count('letter') number of l of astring = ", astring.count("l"))
print("\n")
astring = "Hello world!"
print("MAJUSCULE string.upper()",astring.upper())
print("MINUSCULE string.lower()",astring.lower())

print("\n")

astring = "Hello world!"
print("startswith() return bool",astring.startswith("Hello"))
print("endswith()",astring.endswith("asdfasdfasdf"))


print("------------EXERCICE  9-------------")

print("Conditions");

print("in Operator")

name = 'john'
if name in ["john","Rick"]:
    print("your name is either John or Rick")


print("------------EXERCICE  10-------------")

print("Loops")

primes = [2,3,5,7]
for prime in primes: 
    print(prime),


for x in range(5): 
    print(x), 

for x in range(3,6):
    print(x),

for x in range(3,8,2):
    print(x),



count = 0 
while count < 5: 
    print(count)
    count += 1 



count = 0 
while True: 
    print(count)
    count+=1
    if count >= 5: 
       break 


for x in range(10): 
    if x%2 == 0: 
        continue 
    print(x);





numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

 #Accessing an list using in 
#for number in numbers: 
#    if number == 237: 
#        break
#    
#    if number %2 ==1: 
#        continue 
#    print(number)
#
for number  in numbers: 
    if number <= 237:
        break
    print(number)
       
def my_funtion():
    print("My first Function")
my_funtion()
    

def list_benefits():
    return "More organized code","More readable code", "Easier code reuse","Allowing programmers to share and connect code together"


def build_sentence(data):
    return"%s is a benefit of funtions!" % data


def name_the_benefits_of_funtions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_funtions()


def sum(a,b):
     print(a + b)


sum(250,500)










print("------------EXERCICE  8-------------")

print("------------EXERCICE  8-------------")

























