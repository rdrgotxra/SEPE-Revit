# -*- coding: utf-8 -*-

from pyrevit.versionmgr import updater
from pyrevit import script

logger = script.get_logger()

try:
    updater.check_for_updates()
    logger.info("Extensão verificada e atualizada.")
except Exception as e:
    logger.error("Erro ao atualizar: {}".format(e))
