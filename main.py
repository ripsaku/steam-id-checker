import requests, random, string, bs4, os
import rich
from rich import print
from rich.console import Console
import time
import tkinter as tk
from tkinter import filedialog
import ctypes

def set_console_title(title):
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


webhook = input("Discord Webhook: ")

r = requests.get(webhook)
r.status_code
if r.status_code == 401:
    console.print("Invalid webhook", style="red")
    time.sleep(2.4)
    exit()
os.system("cls")

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select list (.txt)",
    filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
)

if not file_path:
    console.print("No file selected. Exiting.", style="yellow")
    exit()

try:
    with open(file_path, 'r') as archivo:
        palabras_a_probar = [line.strip() for line in archivo]
    total_palabras = len(palabras_a_probar)
    print(f"Loaded {total_palabras} from file: {file_path}")
except FileNotFoundError:
    console.print(f"Error: File not found on path: {file_path}", style="red")
    exit()
except Exception as e:
    console.print(f"Error reading the file: {e}", style="red")
    exit()

palabras_checkeadas = 0

for palabra in palabras_a_probar:
    palabras_checkeadas += 1
    if len(palabra) < 3:
        console.print(f'\r[bold yellow]{palabra}[/bold yellow] IS INVALID (too short)')
    else:
        request = requests.get(f'https://steamcommunity.com/id/{palabra}')
        lxml = bs4.BeautifulSoup(request.content, 'lxml')
        title = lxml.find('title')
        list_title = title.text.split()
        if list_title[-1] == "Error":
            console.print(f'\r[bold green]{palabra}[/bold green] IS AVAILABLE')
            requests.post(webhook, data={"content" : f"\🌠 New ID available `{palabra}` \n remember **it can be banned** or **blacklisted.** >.<\n`--------------------------------`"})
        else:
            console.print(f'\r[bold red]{palabra}[/bold red] IS NOT AVAILABLE')
    progress_text = f"IDs: {palabras_checkeadas}/{total_palabras}"
    set_console_title(progress_text)
    time.sleep(0.1)

console.print("\n\n\n")
console.print(f'[bold magenta]Finished[/bold magenta]')
console.print("\n\n\n")

#Originally made by github.com/Femboysito and github.com/t2zC
#Remade by github.com/ripsaku