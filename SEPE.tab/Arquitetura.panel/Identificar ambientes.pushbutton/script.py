# -*- coding: utf-8 -*-
#! ironpython3

"""Identifica e preenche o parâmetro "Ambiente" todas as paredes do projeto."""

from Autodesk.Revit.DB import (
    XYZ,
    BuiltInParameter,
    FilteredElementCollector,
    Transaction,
    Wall,
)

doc = __revit__.ActiveUIDocument.Document  # é o projeto aberto

OFFSET = 0.003
PARAM_AMBIENTE = "Ambiente"


# retorna um ponto à frente da face externa da parede
def get_point(wall):
    loc = wall.Location

    normal = wall.Orientation.Normalize()
    offset = (wall.Width / 2.0) + OFFSET

    point = loc.Curve.Evaluate(0.5, True)
    point += normal.Multiply(offset)

    bbox = wall.get_BoundingBox(None)
    z_mid = (bbox.Min.Z + bbox.Max.Z) / 2.0

    return XYZ(point.X, point.Y, z_mid)


# lista com parede em todas as fases
def get_walls(doc):
    return (
        FilteredElementCollector(doc)
        .OfClass(Wall)
        .WhereElementIsNotElementType()
        .ToElements()
    )


# pega fase de criação da parede => considerar depois outros elementos
def get_phase(wall, doc):
    phase_id = wall.get_Parameter(BuiltInParameter.PHASE_CREATED).AsElementId()
    return doc.GetElement(phase_id)


# retorna o nome do ambiente, pronto para escrever no parâmetro
def get_ambient_name(point, phase, doc):
    ambient = doc.GetRoomAtPoint(point, phase)

    if ambient is None:
        return None

    return ambient.get_Parameter(BuiltInParameter.ROOM_NAME).AsString()


def set_ambiente(wall, nome):
    param = wall.LookupParameter(PARAM_AMBIENTE)
    if param and not param.IsReadOnly:
        param.Set(nome)
        return True
    return False


def main(doc):
    walls = get_walls(doc)

    # pyrevit envia todos os dados de uma vez só, evitando erros
    with Transaction(doc, "SEPE - Identificar Ambiente") as t:
        t.Start()
        try:
            for wall in walls:
                phase = get_phase(wall, doc)

                point = get_point(wall)
                if point is None:
                    continue

                ambient_name = get_ambient_name(point, phase, doc)
                if ambient_name is None:
                    continue

                set_ambiente(wall, ambient_name)

            t.Commit()

        except Exception as ex:
            t.RollBack()
            print("Erro: {}".format(str(ex)))


main(doc)
