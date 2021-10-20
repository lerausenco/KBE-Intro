import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences


class Arc:

    # Signature CreateArc(center, xDirection, yDirection, radius, startAngle, endAngle)
    def __init__(self, x0, y0, z0, xDirection, yDirection, radius, startAngle, endAngle):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0

        # Expected input for x and y direction vectors is (x, y, z)
        self.xDirection = xDirection
        self.yDirection = yDirection

        self.radius = radius
        self.startAngle = startAngle
        self.endAngle = endAngle

        self.initForNX()

    def initForNX(self):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        #   The Arc
        center = NXOpen.Point3d(float(self.x0), float(self.y0), float(self.z0))
        xDirection = NXOpen.Vector3d(float(self.xDirection[0]), float(
            self.xDirection[1]), float(self.xDirection[2]))
        yDirection = NXOpen.Vector3d(float(self.yDirection[0]), float(
            self.yDirection[1]), float(self.yDirection[2]))

        # Signature CreateArc(center, xDirection, yDirection, radius, startAngle, endAngle)
        self.arc = workPart.Curves.CreateArc(center, xDirection, yDirection, float(
            self.radius), float(self.startAngle) * math.pi/180, float(self.endAngle) * math.pi/180)
        self.body = self.arc
