import subprocess

try:
    result = subprocess.check_output(
        "pyrevit extensions update SEPE-Revit --debug",
        shell=True,
        creationflags=0x08000000,
    )

    result = str(result).lower()

    if "already up-to-date" not in result:
        print("rodrigo!")

except Exception as e:
    print("ERRO ao iniciar update: {}".format(e))
