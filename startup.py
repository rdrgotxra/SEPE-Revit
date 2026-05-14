import subprocess

try:
    subprocess.Popen(
        ["pyrevit", "extensions", "update", "SEPE-Revit"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )
except Exception as e:
    print("ERRO ao iniciar update: {}".format(e))
