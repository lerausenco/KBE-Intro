import sys

#----------------CHANGE TO YOUR PATH
#sys.path.append('C:/Users/lera_/OneDrive/Dokumenter/NTNU/9. H21/KBE StudAss/KBE-Intro')
#-----------------------------------

from Shapes.Block import Block
from Shapes.Cylinder import Cylinder
from Shapes.Sphere import Sphere
from Shapes.Cone import Cone

block = Block(0, 0, 0, 100, 100, 100)

cylinder = Cylinder(0, 0, 0, 10, 50)

sphere = Sphere(200, 0, 0, 100)

cone = Cone(300, 0, 0, 50, 25, 60)

