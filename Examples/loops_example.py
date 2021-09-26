import sys

#----------------CHANGE TO YOUR PATH
sys.path.append('C:/Users/lera_/OneDrive/Dokumenter/NTNU/9. H21/KBE StudAss/KBE-Intro')
#-----------------------------------

from Shapes.Sphere import Sphere

for i in range(1, 10):
    sphere = Sphere(i * 30, i * 15, 0, i * 2)
    #sphere.initForNX()
