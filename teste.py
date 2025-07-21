import subprocess
import platform

sistema_operacional = platform.system()

if sistema_operacional == "Windows":
    subprocess.run(["explorer", "."])
elif sistema_operacional == "Linux":
    subprocess.run(["xdg-open", "."])
elif sistema_operacional == "Darwin":  # macOS
    subprocess.run(["open", "."])
else:
    print("Sistema operacional não suportado")