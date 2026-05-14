import subprocess

from pyrevit import framework

try:
    subprocess.Popen(
        ["pyrevit", "extensions", "update", "--all"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )
except Exception as e:
    framework.debug_print("ERRO ao iniciar update: {}".format(e))
