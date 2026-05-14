import subprocess

try:
    result = subprocess.check_output(
        "pyrevit extensions update SEPE-Revit",
        shell=True,
        creationflags=0x08000000,
    )

    result = str(result).lower()

    if "already up-to-date" not in result:
        print(result)

except Exception as e:
    print("ROD ERRO ao iniciar update: {}".format(e))
