from math import*

class Spheres:
    
    def __init__(self, rad):
        self.radius = rad
        self.surfacearea = 0
        self.volume = 0

    def Radius(self):
        return self.rad

    def SA(self):
        rad= self.radius
        self.surfacearea = (4*pi*(rad*rad))
        return self.surfacearea

    def Vol(self):
        rad= self.radius
        self.volume = ((4/3)*pi*(rad*rad*rad))
        return self.volume
    
def main():
    rad= float(input("Enter the radius of a Sphere: "))
    radius = Spheres(rad)
    print (" The volume of the Sphere is: ", radius.Vol())
    print (" The surface area of the Sphere is: ", radius.SA())

if __name__ == '__main__':
    main()

