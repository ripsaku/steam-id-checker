import requests, random, string, bs4, os
import rich
from rich import print
from rich.console import Console
import time
import tkinter as tk
from tkinter import filedialog
import ctypes

def set_console_title(title):
    """Cambia el título del CMD."""
    ctypes.windll.kernel32.SetConsoleTitleW(title)

console = Console()

os.system("cls")
console.print(f"""\n\n

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠶⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠉⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠉⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⡠⡀⠹⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠀⠄⡀⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠆⡇⠰⠀⠈⠻⠦⠶⠶⠶⠶⠾⠶⠞⠋⠀⡌⠀⡇⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠃⠀⠂⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠁⠀⢻⣅⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⣠⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣂⠀⠀⠀⠀⠀⠀⡿⣝⣺⣯⡏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣏⡀⠀⠀⠀⠀⠀⠘⠫⣷⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⠄⠀⠀⠀⠀⠀⣯⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⣀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡧⠀⠀⠀⠀⠀⠀⠀⢠⣶⡄⠀⠀⠀⠀⠀⠀⠘⠛⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠠⠼⡦⠄⠀⠀⠋⢿⠉⠀
⠀⣨⣧⠄⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠀⠀⠀⠈⠛⠀⠀⠀⠀⠀⠀⠀⠀⠠⠐⠀⠂⠠⠀⢠⠟⠁⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⠂⠀⠀⠀⠀⠀⠀⠹⣧⣄⠀⠀⡒⠉⠉⠈⡃⠀⢰⣆⢠⣶⣄⣼⠀⠐⠠⠀⠒⢁⣴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣄⣿⡆⠀⠀⠀⠀⠀⠘⢿⣇⠀⠈⠀⠂⠐⠁⠀⠀⠛⠛⠁⠈⠀⠀⣀⣤⡴⣷⡛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⢞⣷⠃⠀⠀⠀⠀⠀⠀⠀⠙⢿⡷⠴⢴⡤⢦⠤⡤⠤⠤⠶⠶⠚⠛⠉⠀⠀⢨⣿⣦⣀⢀⣠⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡀⡀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠴⢖⡶⡿⡈⡹⡑⢢⠌⣪⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢻⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡿⠀⠀⠀⠀⠀⠀⠀⠀⠐⢼⣦⣷⠱⢌⡒⡌⡝⣜⠣⣑⠅⠎⠇⣳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⠛⠻⢷⣤⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠘⢷⣄⠀⠀⠉⣿⡐⠢⡔⡘⡡⢇⡡⢅⢡⡙⣬⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣆⡀⠀⢻⣧⠀⠀⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠙⠻⣶⣤⡿⠙⢧⣆⠵⡁⠦⠇⡪⢠⣜⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣦⠀⠹⢾⣀⡀⠀⢹⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⡾⣅⡎⢆⣇⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⠀⠀⠉⠛⠛⢾⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠛⠻⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⢲⣶⣶⣤⣼⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢸⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡴⢾⣿⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠄⠀⠀⠀⣤⠶⠓⠋⠉⠁⠀⢈⣿⠀⠀⢼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡆⠀⠀⠸⣿⠁⠀⠀⠀⠀⠀⠨⢿⣀⣀⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣄⣀⣰⠟⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\n""", style="purple")


#Importar webhook
webhook = input("Discord Webhook: ")

#Revisar webhook
r = requests.get(webhook)
r.status_code
if r.status_code == 401:
    console.print("Webhook no válido", style="red")
    time.sleep(2.4)
    exit()
os.system("cls")

#Leer la lista de palabras abriendo un explorador de archivos
root = tk.Tk()
root.withdraw() # Oculta la ventana principal de tkinter

file_path = filedialog.askopenfilename(
    title="Seleccionar archivo de lista de palabras (.txt)",
    filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
)

if not file_path:
    console.print("No se seleccionó ningún archivo. Saliendo.", style="yellow")
    exit()

try:
    with open(file_path, 'r') as archivo:
        palabras_a_probar = [line.strip() for line in archivo]
    total_palabras = len(palabras_a_probar)
    print(f"Se cargaron {total_palabras} palabras del archivo: {file_path}")
except FileNotFoundError:
    console.print(f"Error: No se encontró el archivo en la ruta: {file_path}", style="red")
    exit()
except Exception as e:
    console.print(f"Ocurrió un error al leer el archivo: {e}", style="red")
    exit()

palabras_checkeadas = 0

#Check
for palabra in palabras_a_probar:
    palabras_checkeadas += 1
    if len(palabra) < 3:
        console.print(f'\r[bold yellow]{palabra}[/bold yellow] ES INVALIDO (demasiado corta)')
    else:
        request = requests.get(f'https://steamcommunity.com/id/{palabra}')
        lxml = bs4.BeautifulSoup(request.content, 'lxml')
        title = lxml.find('title')
        list_title = title.text.split()
        if list_title[-1] == "Error":
            console.print(f'\r[bold green]{palabra}[/bold green] ESTÁ DISPONIBLE')
            requests.post(webhook, data={"content" : f"\🌠 Nueva ID disponible `{palabra}` \n recuerda **puede estar baneada** o **blacklisteada.** >.<\n`--------------------------------`"})
        else:
            console.print(f'\r[bold red]{palabra}[/bold red] NO ESTÁ DISPONIBLE')
    progress_text = f"Palabras: {palabras_checkeadas}/{total_palabras}"
    set_console_title(progress_text) # Título ventana
    time.sleep(0.1)

console.print("\n\n\n")
console.print(f'[bold magenta]Finalizado[/bold magenta]')
console.print("\n\n\n")

#Hecho originalmente por github.com/t2zC
#Rehecho por @dvfb en discord