class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        area = 3.14 * (self.radius**2)
        return area

    def perimeter(self):
        perimeter = 2 * 3.14 * (self.radius**2)
        return perimeter
        
class Square:
    def __init__(self,side):
        self.side = side
    
    def area(self):
        area =(self.side**2)
        return area

    def perimeter(self):
        perimeter = 4 * (self.side)
        return perimeter

class Rectangle:
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def area(self):
        area = (self.length)*(self.width)
        return area

    def perimeter(self):
        perimeter = 2 * (self.length+self.width)
        return perimeter


class Sphere:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        area = 4 * 3.14 * (self.radius**2)
        return area

    def volume(self):
        volume = 4%3 * 3.14 * (self.radius**3)
        return volume
