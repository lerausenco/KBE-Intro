import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences


class Line:

    def __init__(self, x0, y0, z0, x1, y1, z1):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0

        self.x1 = x1
        self.y1 = y1
        self.z1 = z1

        self.initForNX()

    def initForNX(self):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        #   The Line
        p0 = NXOpen.Point3d(float(self.x0), float(self.y0), float(self.z0))
        p1 = NXOpen.Point3d(float(self.x1), float(self.y1), float(self.z1))

        self.line = workPart.Curves.CreateLine(p0, p1)
        self.body = self.line
