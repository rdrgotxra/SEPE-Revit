"""Identifica e preenche o parâmetro "Ambiente" todas as paredes do projeto."""

# -*- coding: utf-8 -*-
#! ironpython3

from Autodesk.Revit.DB import (
    BuiltInParameter,
    FilteredElementCollector,
    LocationCurve,
    Transaction,
    UnitTypeId,
    UnitUtils,
    Wall,
)

doc = __revit__.ActiveUIDocument.Document

OFFSET = UnitUtils.ConvertToInternalUnits(0.30, UnitTypeId.Meters)
PARAM_AMBIENTE = "Ambiente"


def get_point(wall):
    loc = wall.Location
    if not isinstance(loc, LocationCurve):
        return None
    point = loc.Curve.Evaluate(0.5, True)
    normal = wall.Orientation.Normalize()
    return point + normal.Multiply(OFFSET)


def get_walls(doc):
    return (
        FilteredElementCollector(doc)
        .OfClass(Wall)
        .WhereElementIsNotElementType()
        .ToElements()
    )


def get_phase(wall, doc):
    phase_id = wall.get_Parameter(BuiltInParameter.PHASE_CREATED).AsElementId()
    return doc.GetElement(phase_id)


def get_ambiente(point, phase, doc):
    return doc.GetRoomAtPoint(point, phase)


def set_ambiente(wall, nome):
    param = wall.LookupParameter(PARAM_AMBIENTE)
    if param and not param.IsReadOnly:
        param.Set(nome)
        return True
    return False


def main(doc):
    walls = get_walls(doc)

    with Transaction(doc, "SEPE - Identificar Ambiente") as t:
        t.Start()
        try:
            for wall in walls:
                point = get_point(wall)
                if point is None:
                    continue

                phase = get_phase(wall, doc)
                ambiente = get_ambiente(point, phase, doc)
                if ambiente is None:
                    continue

                ambiente_nome = ambiente.get_Parameter(
                    BuiltInParameter.ROOM_NAME
                ).AsString()
                param = wall.LookupParameter(PARAM_AMBIENTE)

                if param and not param.IsReadOnly:
                    param.Set(ambiente_nome)

                set_ambiente(wall, ambiente_nome)

            t.Commit()

        except Exception as ex:
            t.RollBack()
            print("Erro: {}".format(str(ex)))


main(doc)
