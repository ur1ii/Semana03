import os
from colorama import Fore, Style
import subprocess
while True:
    try:
        subprocess.run("cls",shell=True)
        edad = int(input("Edad: "))
        break
    except ValueError:
        print(Fore.RED + "Ingresa un valor numérico", Style.RESET_ALL)
        subprocess.run("pause", shell=True)
print(Fore.GREEN + "Edad registrada:", edad, Style.RESET_ALL)
