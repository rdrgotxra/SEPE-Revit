import subprocess

try:
    subprocess.call(
        "pyrevit extensions update SEPE-Revit", shell=True, creationflags=0x08000000
    )

except Exception as e:
    print("ERRO ao iniciar update: {}".format(e))
