import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

class Block:

    def getVolume(self):
        return self.length * self.width * self.height

    def __init__(self, x, y, z, length, width, height, xdirection=[1, 0, 0], ydirection=[0,1,0], color='RED', material='Steel'):
        self.x = x
        self.y = y
        self.z = z
        self.length = length  # instance variable unique to each instance
        self.width = width
        self.height = height

        self.xdirection = NXOpen.Vector3d(float(xdirection[0]), float(xdirection[1]),float(xdirection[2]))
													 
        self.ydirection = NXOpen.Vector3d(float(ydirection[0]), float(ydirection[1]), float(ydirection[2]))
        self.color = color
        self.material = material
        
        self.initForNX()

    def initForNX(self):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        #   The block
        blockfeaturebuilder1 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Block.Null)
        blockfeaturebuilder1.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths

        origBlock = NXOpen.Point3d(float(self.x), float(self.y), float(self.z))
        blockfeaturebuilder1.SetOriginAndLengths(origBlock, str(self.length), str(self.width), str(self.height))
        blockfeaturebuilder1.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
        blockfeaturebuilder1.SetOrientation(self.xdirection, self.ydirection)


        self.body = blockfeaturebuilder1.Commit().GetBodies()[0]
        blockfeaturebuilder1.Destroy()

    def subtract(self, tool):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        subtractfeaturebuilder1 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)

        subtractfeaturebuilder1.Target = self.body  # bodyTarget_.GetBodies()[0] # From where to subtract
        subtractfeaturebuilder1.Tool = tool.body  # What to subtract
        subtractfeaturebuilder1.Operation = NXOpen.Features.FeatureBooleanType.Subtract

        subtractfeaturebuilder1.Commit()
        subtractfeaturebuilder1.Destroy()
