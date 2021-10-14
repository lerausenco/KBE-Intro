import sys

#----------------CHANGE TO YOUR PATH
sys.path.append('C:/Users/lera_/OneDrive/Dokumenter/NTNU/9. H21/KBE StudAss/KBE-Intro')
#-----------------------------------

from Shapes.Block import Block
from Shapes.Sphere import Sphere
from Shapes.Cylinder import Cylinder
from Shapes.Cone import Cone

sphere = Sphere(10, 10, 50, 25)

cyl = Cylinder(10, 10, 50, 20, 12.5, [0,1,0])

sphere.subtract(cyl)

