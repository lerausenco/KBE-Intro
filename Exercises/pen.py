import sys

#----------------CHANGE TO YOUR PATH
sys.path.append(r'C:/Users/lera_/OneDrive/Dokumenter/NTNU/9. H21/KBE StudAss/KBE-Intro')
#-----------------------------------

from Shapes.Sphere import Sphere
from Shapes.Cylinder import Cylinder
from Shapes.Cone import Cone

cone = Cone(0, 0, -30, 1, 10, 30)


cyl = Cylinder(0, 0, 0, 10, 150)

sphere = Sphere(0, 0, 150, 10)


