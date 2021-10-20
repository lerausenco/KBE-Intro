import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences


class Swept:

    def __init__(self, guide, section):

        # guide and section are expected of the form [elem1, elem2, ..., elemN], where elemX is either Line or Arc.

        self.guide = guide
        self.section = section

        self.initForNX()

    def initForNX(self):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        #   The block
        sweptBuilder = workPart.Features.CreateSweptBuilder(
            NXOpen.Features.Swept.Null)

        sweptBuilder.G0Tolerance = 0.01

        sweptBuilder.G1Tolerance = 0.5

        sweptBuilder.PreserveShapeOption = False

        section1 = workPart.Sections.CreateSection(
            0.0094999999999999998, 0.01, 0.5)

        sweptBuilder.SectionList.Append(section1)

        section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)

        selectionIntentRuleOptions1 = workPart.ScRuleFactory.CreateRuleOptions()

        selectionIntentRuleOptions1.SetSelectedFromInactive(False)

        curves1 = []  # [NXOpen.IBaseCurve.Null] * 1
        for curve in self.section:
            cur = curve.body
            curves1.append(cur)

        arc1 = self.section[0].body
        curves1[0] = arc1
        curveDumbRule1 = workPart.ScRuleFactory.CreateRuleBaseCurveDumb(
            curves1, selectionIntentRuleOptions1)

        selectionIntentRuleOptions1.Dispose()
        section1.AllowSelfIntersection(False)

        section1.AllowDegenerateCurves(False)

        rules1 = [None] * 1
        rules1[0] = curveDumbRule1
        helpPoint1 = NXOpen.Point3d(-5.5360108177506895, -
                                    49.677187889044809, 0.0)
        section1.AddToSection(rules1, arc1, NXOpen.NXObject.Null,
                              NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)

        section2 = workPart.Sections.CreateSection(
            0.0094999999999999998, 0.01, 0.5)

        sweptBuilder.GuideList.Append(section2)

        section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)

        selectionIntentRuleOptions2 = workPart.ScRuleFactory.CreateRuleOptions()

        selectionIntentRuleOptions2.SetSelectedFromInactive(False)

        curves2 = []  # [NXOpen.IBaseCurve.Null] * len(self.guide)
        for curve in self.guide:
            cur = curve.body
            curves2.append(cur)

        line1 = self.guide[0].line

        curveDumbRule2 = workPart.ScRuleFactory.CreateRuleBaseCurveDumb(
            curves2, selectionIntentRuleOptions2)

        rules2 = [None] * 1
        rules2[0] = curveDumbRule2
        helpPoint2 = NXOpen.Point3d(
            3.5527136788005009e-15, 3.5527136788005009e-15, 87.501707636101486)
        section2.AddToSection(rules2, line1, NXOpen.NXObject.Null,
                              NXOpen.NXObject.Null, helpPoint2, NXOpen.Section.Mode.Create, False)

        self.body = sweptBuilder.Commit().GetBodies()[0]

        sweptBuilder.Destroy()

    def subtract(self, tool):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        subtractfeaturebuilder1 = workPart.Features.CreateBooleanBuilder(
            NXOpen.Features.BooleanFeature.Null)

        # bodyTarget_.GetBodies()[0] # From where to subtract
        subtractfeaturebuilder1.Target = self.body
        subtractfeaturebuilder1.Tool = tool.body  # What to subtract
        subtractfeaturebuilder1.Operation = NXOpen.Features.FeatureBooleanType.Subtract

        subtractfeaturebuilder1.Commit()
        subtractfeaturebuilder1.Destroy()
