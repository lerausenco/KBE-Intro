import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

class Block:

    def getVolume(self):
        return self.length * self.width * self.height

    def __init__(self, x, y, z, length, width, height, direction=[0, 0, 1], color='RED', material='Steel'):
        self.x = x
        self.y = y
        self.z = z
        self.length = length  # instance variable unique to each instance
        self.width = width
        self.height = height

        self.direction = direction
        self.color = color
        self.material = material

    def initForNX(self):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        #   The block
        blockfeaturebuilder1 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Block.Null)
        blockfeaturebuilder1.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths

        origBlock = NXOpen.Point3d(float(self.x), float(self.y), float(self.z))
        blockfeaturebuilder1.SetOriginAndLengths(origBlock, str(self.length), str(self.width), str(self.height))
        blockfeaturebuilder1.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create

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
