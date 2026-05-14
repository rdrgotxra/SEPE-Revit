import subprocess

from pyrevit.loader import sessionmgr

try:
    subprocess.call(
        "pyrevit extensions update SEPE-Revit", shell=True, creationflags=0x08000000
    )
    sessionmgr.reload_pyrevit()

except Exception as e:
    print("ERRO ao iniciar update: {}".format(e))
