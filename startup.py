from pyrevit.versionmgr import updater

try:
    # Atualiza apenas extensão específica
    updater.update_extension("SEPE-Revit")
except Exception as e:
    # Tratamento específico para sua extensão
    from pyrevit import framework

    framework.debug_print("Falha ao atualizar SEPE-Revit: {}".format(e))
