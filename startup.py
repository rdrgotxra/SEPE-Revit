import subprocess

try:
    subprocess.Popen(
        ["pyrevit", "extensions", "update", "--all"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )

except:
    pass
