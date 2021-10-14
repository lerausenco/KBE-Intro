import sys

#----------------CHANGE TO YOUR PATH
sys.path.append(r'C:/Users/lera_/OneDrive/Dokumenter/NTNU/9. H21/KBE StudAss/KBE-Intro')
#-----------------------------------

from Shapes.Block import Block

total_height = 0
for i in range(10, 0, -1):
    blockN = Block(-10 * i / 2, -10 * i / 2, total_height, i * 10, i * 10, i * 10)
    total_height += i * 10

