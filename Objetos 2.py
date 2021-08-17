#Create a class called Shape. Define a method in it called what_am_i that prints "I am a shape" when called.
#Change your Square and Rectangle classes from the previous challenges to inherit from Shape.
#Create Square and Rectangle objects, and call the new method on both of them.
"""
class Shape():
    def __init__(self,name):
        self.name=name

    def what_am_i(self):
        print("i am a shape")

class Rectangle(Shape):
    rectangles=[]
    def __init__(self,s1,s2):
        self.s1=s1
        self.s2=s2
        self.rectangles.append((self.s1,self.s2))
    def calculate_perimeter(self,s1,s2):
        return s1*2 + s2*2



class Square(Rectangle):
    squares=[]
    def __init__(self,s1):
        self.s1=s1
        self.squares.append(self.s1)
    
    def calculate_perimeter(self,s1,s2):
        return s1*4

R1=Rectangle(4,2)
S1=Square(2)

S1.what_am_i()


R1.calculate_perimeter(4,2)
S1.calculate_perimeter(2,2)

print(Rectangle.rectangles)
"""

#Add a square_list class variable to a class called Square and set your class up so that...
#...every time you create a new Square object, the new object gets added to the square_list.
"""

class Square():
    square_list=[]
    def __init__(self,s1):
        self.s1=s1
        self.square_list.append(self.s1)

S1=Square(2)
S2=Square(7)

print(Square.square_list)

"""
"""
class Square:
    
    def __init__(self,s1):
        self.s1=s1
        
    def __repr__(self):
        return str(self.s1) + " by " + str(self.s1) + " by " + str(self.s1) + " by " + str(self.s1)

print(Square(29))
"""

"""
class greeting:
    def __init__(self):
        self.words="Hello"


def are_the_same(a,b):
    if a is b:
        return True
    else:
        return False
    
g1=greeting()

o1=g1
o2=greeting()

print(are_the_same(o1,o2))

"""
