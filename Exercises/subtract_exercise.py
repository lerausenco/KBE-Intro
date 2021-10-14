import sys

#----------------CHANGE TO YOUR PATH
sys.path.append(r'C:/Users/lera_/OneDrive/Dokumenter/NTNU/9. H21/KBE StudAss/KBE-Intro')
#-----------------------------------

from Shapes.Sphere import Sphere
from Shapes.Cylinder import Cylinder
from Shapes.Block import Block

block = Block(5, 5, 0, 10, 10, 20)


cyl = Cylinder(x=10, y=10, z=0, diameter=20, height=12.5)


cyl2 = Cylinder(x=0, y=10, z=cyl.height / 2, diameter=5, height=cyl.diameter, direction=[1, 0, 0])


cyl3 = Cylinder(x=10, y=0, z=cyl.height / 2, diameter=5, height=cyl.diameter, direction=[0, 1, 0])


cyl.subtract(block)
cyl.subtract(cyl2)
cyl.subtract(cyl3)
