import math as math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences


class Cylinder:

    def __init__(self, x, y, z, diameter, height, direction = [0, 0, 1]):
        self.x = x
        self.y = y
        self.z = z
        self.diameter = diameter  # instance variable unique to each instance
        self.height = height
        self.direction = direction
        
        self.initForNX()

    def initForNX(self):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        #   The cylinder
        cylinderbuilder1 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Cylinder.Null)

        cylinderbuilder1.Diameter.RightHandSide = str(self.diameter)  # Writing the right hand side of the expression
        cylinderbuilder1.Height.RightHandSide = str(self.height)
        cylinderbuilder1.Origin = NXOpen.Point3d(float(self.x), float(self.y), float(self.z))
        cylinderbuilder1.Direction = NXOpen.Vector3d(float(self.direction[0]), float(self.direction[1]),
                                                     float(self.direction[2]))
        cylinderbuilder1.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create

        self.body = cylinderbuilder1.Commit().GetBodies()[0]
        cylinderbuilder1.Destroy()

    def subtract(self, tool):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        subtractfeaturebuilder1 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)

        subtractfeaturebuilder1.Target = self.body  # bodyTarget_.GetBodies()[0] # From where to subtract
        subtractfeaturebuilder1.Tool = tool.body  # What to subtract
        subtractfeaturebuilder1.Operation = NXOpen.Features.FeatureBooleanType.Subtract

        subtractfeaturebuilder1.Commit()
        subtractfeaturebuilder1.Destroy()
