## Part 1
try:
    #Index Error
    l1=[0,1,2,3]
    print(l1[5])

    #Type Error
    a="Hello"
    b="World"
    print(l1[a:b])

    #Zero div Error
    a=0
    print(10/a)

    #IO Error
    f = open("random.txt",'r')

    #Assertion Error
    x = 1
    y = 0
    assert y != 0, "Invalid Operation"
    print(x / y)

except IndexError:
    print("Error index out of bounds")

except TypeError:
    print("Error not an integer")

except ZeroDivisionError:
    print("Error cant divide by 0 ")

except IOError:
    print("Error File not found")

except AssertionError as msg:
    print(msg)
    
## Part 2
class DefaulterError(Exception):

    def __init__(self):
        print("Your Marks and attendance are less than 75!")

class Student:

    def __init__(self, name, attendance, marks):
        self.name = name
        self.attendance = attendance
        self.marks = marks
    
    def find_defaulter(self):
        try:
            if self.attendance<75 and self.marks<75:
                raise DefaulterError()

        except DefaulterError:
            print("DefaulterError")

s1 = Student("Mareena", 0, 50)
s1.find_defaulter()
