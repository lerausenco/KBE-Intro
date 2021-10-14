import sys

##your path here
sys.path.append(r'C:/Users/lera_/OneDrive/Dokumenter/NTNU/9. H21/KBE StudAss/KBE-Intro')
##
from Shapes.Swept import Swept
from Shapes.Line import Line
from Shapes.Arc import Arc

line = Line(0, 0, 0, 0, 0, 100)
arc = Arc(0, 0, 0, (1, 0, 0), (0, 1, 0), 50, 0, 360)

#
swept = Swept([line], [arc])
