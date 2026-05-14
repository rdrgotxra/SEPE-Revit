from pyrevit.versionmgr import updater

try:
    updater.update_extension("SEPE-Revit")

except Exception as e:
    from pyrevit import framework

    framework.debug_print("Falha ao atualizar SEPE-Revit: {}".format(e))
