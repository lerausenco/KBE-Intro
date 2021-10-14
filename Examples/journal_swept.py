# NX 1911
# Journal created by lera_ on Wed Oct 13 19:26:00 2021 W. Europe Summer Time
#
import math
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: Insert->Sweep->Swept...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sweptBuilder1 = workPart.Features.CreateSweptBuilder(NXOpen.Features.Swept.Null)
    
    unit1 = sweptBuilder1.ScalingMethod.PerimeterLaw.Value.Units
    
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sweptBuilder1.G0Tolerance = 0.01
    
    sweptBuilder1.G1Tolerance = 0.5
    
    sweptBuilder1.PreserveShapeOption = False
    
    sweptBuilder1.OrientationMethod.AngularLaw.Value.SetFormula("0")
    
    sweptBuilder1.OrientationMethod.AngularLaw.StartValue.SetFormula("0")
    
    sweptBuilder1.OrientationMethod.AngularLaw.EndValue.SetFormula("0")
    
    sweptBuilder1.ScalingMethod.AreaLaw.Value.SetFormula("1")
    
    sweptBuilder1.ScalingMethod.AreaLaw.StartValue.SetFormula("1")
    
    sweptBuilder1.ScalingMethod.AreaLaw.EndValue.SetFormula("1")
    
    sweptBuilder1.ScalingMethod.PerimeterLaw.Value.SetFormula("1")
    
    sweptBuilder1.ScalingMethod.PerimeterLaw.StartValue.SetFormula("1")
    
    sweptBuilder1.ScalingMethod.PerimeterLaw.EndValue.SetFormula("1")
    
    theSession.SetUndoMarkName(markId1, "Swept Dialog")
    
    sweptBuilder1.Spine.DistanceTolerance = 0.01
    
    sweptBuilder1.Spine.ChainingTolerance = 0.0094999999999999998
    
    sweptBuilder1.AlignmentMethod.AlignCurve.DistanceTolerance = 0.01
    
    sweptBuilder1.AlignmentMethod.AlignCurve.ChainingTolerance = 0.0094999999999999998
    
    sweptBuilder1.OrientationMethod.OrientationCurve.DistanceTolerance = 0.01
    
    sweptBuilder1.OrientationMethod.OrientationCurve.ChainingTolerance = 0.0094999999999999998
    
    sweptBuilder1.OrientationMethod.AngularLaw.AlongSpineData.Spine.DistanceTolerance = 0.01
    
    sweptBuilder1.OrientationMethod.AngularLaw.AlongSpineData.Spine.ChainingTolerance = 0.0094999999999999998
    
    sweptBuilder1.OrientationMethod.AngularLaw.LawCurve.DistanceTolerance = 0.01
    
    sweptBuilder1.OrientationMethod.AngularLaw.LawCurve.ChainingTolerance = 0.0094999999999999998
    
    sweptBuilder1.ScalingMethod.ScalingCurve.DistanceTolerance = 0.01
    
    sweptBuilder1.ScalingMethod.ScalingCurve.ChainingTolerance = 0.0094999999999999998
    
    sweptBuilder1.ScalingMethod.AreaLaw.AlongSpineData.Spine.DistanceTolerance = 0.01
    
    sweptBuilder1.ScalingMethod.AreaLaw.AlongSpineData.Spine.ChainingTolerance = 0.0094999999999999998
    
    sweptBuilder1.ScalingMethod.AreaLaw.LawCurve.DistanceTolerance = 0.01
    
    sweptBuilder1.ScalingMethod.AreaLaw.LawCurve.ChainingTolerance = 0.0094999999999999998
    
    sweptBuilder1.ScalingMethod.PerimeterLaw.AlongSpineData.Spine.DistanceTolerance = 0.01
    
    sweptBuilder1.ScalingMethod.PerimeterLaw.AlongSpineData.Spine.ChainingTolerance = 0.0094999999999999998
    
    sweptBuilder1.ScalingMethod.PerimeterLaw.LawCurve.DistanceTolerance = 0.01
    
    sweptBuilder1.ScalingMethod.PerimeterLaw.LawCurve.ChainingTolerance = 0.0094999999999999998
    
    sweptBuilder1.Spine.AngleTolerance = 0.5
    
    sweptBuilder1.AlignmentMethod.AlignCurve.AngleTolerance = 0.5
    
    sweptBuilder1.OrientationMethod.OrientationCurve.AngleTolerance = 0.5
    
    sweptBuilder1.OrientationMethod.AngularLaw.AlongSpineData.Spine.AngleTolerance = 0.5
    
    sweptBuilder1.OrientationMethod.AngularLaw.LawCurve.AngleTolerance = 0.5
    
    sweptBuilder1.ScalingMethod.ScalingCurve.AngleTolerance = 0.5
    
    sweptBuilder1.ScalingMethod.AreaLaw.AlongSpineData.Spine.AngleTolerance = 0.5
    
    sweptBuilder1.ScalingMethod.AreaLaw.LawCurve.AngleTolerance = 0.5
    
    sweptBuilder1.ScalingMethod.PerimeterLaw.AlongSpineData.Spine.AngleTolerance = 0.5
    
    sweptBuilder1.ScalingMethod.PerimeterLaw.LawCurve.AngleTolerance = 0.5
    
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    sweptBuilder1.SectionList.Append(section1)
    
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves1 = [NXOpen.IBaseCurve.Null] * 1 
    arc1 = workPart.Arcs.FindObject("ENTITY 5 3 1")
    curves1[0] = arc1
    curveDumbRule1 = workPart.ScRuleFactory.CreateRuleBaseCurveDumb(curves1)
    
    section1.AllowSelfIntersection(False)
    
    rules1 = [None] * 1 
    rules1[0] = curveDumbRule1
    helpPoint1 = NXOpen.Point3d(19.424303336337555, -46.045101959909267, 0.0)
    section1.AddToSection(rules1, arc1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId3, None)
    
    sections1 = [NXOpen.Section.Null] * 1 
    sections1[0] = section1
    sweptBuilder1.AlignmentMethod.SetSections(sections1)
    
    expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId2, None)
    
    section2 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    sweptBuilder1.GuideList.Append(section2)
    
    section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves2 = [NXOpen.IBaseCurve.Null] * 1 
    line1 = workPart.Lines.FindObject("ENTITY 3 1 1")
    curves2[0] = line1
    curveDumbRule2 = workPart.ScRuleFactory.CreateRuleBaseCurveDumb(curves2)
    
    section2.AllowSelfIntersection(False)
    
    rules2 = [None] * 1 
    rules2[0] = curveDumbRule2
    helpPoint2 = NXOpen.Point3d(0.0, 3.5527136788005009e-15, 81.420754898218576)
    section2.AddToSection(rules2, line1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint2, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId5, None)
    
    sweptBuilder1.ScalingMethod.AreaLaw.AlongSpineData.SetFeatureSpine(section2)
    
    sweptBuilder1.ScalingMethod.PerimeterLaw.AlongSpineData.SetFeatureSpine(section2)
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Update Law Data")
    
    theSession.DeleteUndoMarksUpToMark(markId6, "Update Law Data", False)
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Update Law Data")
    
    theSession.DeleteUndoMarksUpToMark(markId7, "Update Law Data", False)
    
    sweptBuilder1.OrientationMethod.AngularLaw.AlongSpineData.SetFeatureSpine(section2)
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Update Law Data")
    
    theSession.DeleteUndoMarksUpToMark(markId8, "Update Law Data", False)
    
    theSession.DeleteUndoMark(markId4, None)
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Swept")
    
    theSession.DeleteUndoMark(markId9, None)
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Swept")
    
    nXObject1 = sweptBuilder1.Commit()
    
    displayModification1 = theSession.DisplayManager.NewDisplayModification()
    
    displayModification1.ApplyToAllFaces = False
    
    displayModification1.SetNewGrid(0, 0)
    
    displayModification1.PoleDisplayState = False
    
    displayModification1.KnotDisplayState = False
    
    objects1 = [NXOpen.DisplayableObject.Null] * 1 
    swept1 = nXObject1
    face1 = swept1.FindObject("FACE 2 {(-0.0327082929034,0,100) SWEPT(1)}")
    objects1[0] = face1
    displayModification1.Apply(objects1)
    
    face1.Color = 32767
    
    displayModification1.SetNewGrid(0, 0)
    
    displayModification1.PoleDisplayState = False
    
    displayModification1.KnotDisplayState = False
    
    objects2 = [NXOpen.DisplayableObject.Null] * 1 
    face2 = swept1.FindObject("FACE 1 {(-0.0327082929034,0,0) SWEPT(1)}")
    objects2[0] = face2
    displayModification1.Apply(objects2)
    
    face2.Color = 32767
    
    displayModification1.SetNewGrid(0, 0)
    
    displayModification1.PoleDisplayState = False
    
    displayModification1.KnotDisplayState = False
    
    objects3 = [NXOpen.DisplayableObject.Null] * 1 
    face3 = swept1.FindObject("FACE 10001 {(-50,0,50) SWEPT(1)}")
    objects3[0] = face3
    displayModification1.Apply(objects3)
    
    face3.Color = 32767
    
    theSession.DeleteUndoMark(markId10, None)
    
    theSession.SetUndoMarkName(markId1, "Swept")
    
    sweptBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression4)
    
    workPart.Expressions.Delete(expression1)
    
    workPart.Expressions.Delete(expression2)
    
    workPart.Expressions.Delete(expression3)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()