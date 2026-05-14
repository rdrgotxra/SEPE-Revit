import subprocess

try:
    subprocess.Popen(
        "pyrevit extensions update SEPE-Revit",
        creationflags=0x08000000,
    )
except Exception as e:
    print("ERRO ao iniciar update: {}".format(e))
