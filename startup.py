import subprocess

try:
    subprocess.call(["pyrevit", "extensions", "update", "SEPE-Revit"])
except Exception as e:
    print("ERRO ao iniciar update: {}".format(e))
