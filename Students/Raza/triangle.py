class Triangle:
    def __init__(self, angle1, angle2, angle3):
        self.sides = 3
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        self.type = ""
    def checkIfRight(self): # getter (we are just getting information (not updating anything))
        if self.angle1 == 90 or self.angle2 == 90 or self.angle3 == 90:
            return True
        return False
    def setTriangleType(self): # setter (setting the type, not returning anything)
        if self.angle1 == self.angle2 == self.angle3:
            self.type = "Equilateral"
        elif self.angle1 == 90 or self.angle2 == 90 or self.angle3 == 90:
            self.type = "Right"
    def changeAngle(self, angleNumber, newAngle): # setter
        if angleNumber == 1:
            self.angle1 = newAngle
        if angleNumber == 2:
            self.angle2 = newAngle
        if angleNumber == 3:
            self.angle3 = newAngle

def main():
    # Create a class with a method that returns true if the triangle is a right a triangle.
    t1 = Triangle(90, 30, 60) # this is an object, an instance of the Triangle class
    print(t1.checkIfRight()) # getting a True/False value depending on whether it is a right triangle
    t1.changeAngle(1, 30) # calling changeAngle METHOD and passing in the angleNumber and newAngle.
    print(t1.angle1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()