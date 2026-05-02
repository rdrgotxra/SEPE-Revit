import subprocess

try:
    returncode = subprocess.call(["pyrevit", "extensions", "update", "SEPE-Revit"])

    if returncode != 0:
        print("Erro ao atualizar.")

except Exception as e:
    print("Erro ao atualizar.", e)
