import sys

#----------------CHANGE TO YOUR PATH
sys.path.append(r'C:/Users/lera_/OneDrive/Dokumenter/NTNU/9. H21/KBE StudAss/KBE-Intro')
#-----------------------------------

from Shapes.Block import Block
from Shapes.Cone import Cone
from Shapes.Cylinder import Cylinder

screw_width = 5
screw_head_width = 15
screw_length = 60
track_width = screw_head_width*0.1
track_length = screw_head_width*0.6

head = Cone(0, 0, -5, screw_head_width, screw_width, 5)


body = Cylinder(0, 0, 0, screw_width, screw_length)


bottom = Cone(0, 0, body.height, screw_width, 1, 5)


x_track = Block(-track_length/2,
              -track_width/2, head.z, track_length,
              head.baseDiameter*0.1, head.baseDiameter*0.1)


y_track = Block(-track_width/2, -track_length/2,
               head.z, head.baseDiameter*0.1, track_length,
               head.baseDiameter*0.1)


head.subtract(x_track)
head.subtract(y_track)

points = [x for x in range(head.z+head.height*2, screw_length)]

for point in points:
    cyl =  Cylinder(0, 0, point, screw_width*1.2, height=0.2, direction=[0,1,1.5])
 
