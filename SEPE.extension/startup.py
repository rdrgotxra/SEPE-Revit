import subprocess

try:
    result = subprocess.run(
        ["pyrevit", "extensions", "update", "SEPE-Revit"],
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        print("Erro ao atualizar.")
        if result.stderr:
            print(result.stderr)

except Exception as e:
    print("Erro ao atualizar.", e)
