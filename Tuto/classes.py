
class MyClass: 
    variable = "blaaa"

    def funtion(self):
        print("this is a massage inside a class")

myobjectx = MyClass()
myobjecty = MyClass()

print(myobjectx.variable)


myobjecty.variable ="yakity"


print(myobjectx.variable)
print(myobjecty.variable)


myobjectx.funtion()

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


# your code goes here

car1 = Vehicle()
car2 = Vehicle()

car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000

car2.name = "Jump"
car2.kind = "van"
car2.value = 10000
car2.color = "blue"



# test code
print(car1.description())
print(car2.description())























