import os
from colorama import Fore, Style
import subprocess
while True:
    try:
        subprocess.run("cls",shell=True)
        edad = int(input("Edad: "))
        break
    except ValueError:
        print("Ingresa un valor numérico")
        subprocess("pause")
print(Fore.GREEN + "Edad registrada:", edad, Style.RESET_ALL)
