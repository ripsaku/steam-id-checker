import requests, random, string, bs4, os
import rich
from rich import print
from rich.console import Console
import time
import tkinter as tk
from tkinter import filedialog
import ctypes
import datetime
import json
from pypresence import Presence
import sys
import pathlib 

# --- Pause Parameters ---
StopQnt = 25  # Checks until pause
StopTime = 60 # Seconds of pause
# --------------------------

# --- Discord RPC ---
CLIENT_ID = '1436813537665355897'
# --------------------------

def set_console_title(title):
    if sys.platform == 'win32':
        ctypes.windll.kernel32.SetConsoleTitleW(title)

console = Console()

os.system("cls")

# --- LECTURA DEL ARTE ASCII ---
ascii_art = "<3"

try:
    with open("ASCII.txt", "r", encoding="utf-8") as f:
        ascii_art = f.read()
except FileNotFoundError:
    console.print("[bold red]Error:[/bold red] File 'ASCII.txt' not found. Using default placeholder.", style="red")
except Exception as e:
    console.print(f"[bold red]Error reading ASCII.txt:[/bold red] {e}", style="red")

# Aplicamos el estilo 'purple' al arte
console.print(f"""\n\n{ascii_art}\n""", style="purple") 
# ------------------------------

console.print(f"[bold magenta][0][/bold magenta][magenta] No webhook (results exported into .txt)[/magenta]")
console.print(f"[bold magenta][1][/bold magenta][magenta] Discord Webhook (results through Discord messages)[/magenta]")
console.print(f"[bold magenta][2][/bold magenta][magenta] Telegram Bot Api (results through Telegram messages)[/magenta]")
console.print(f"[bold magenta]Choose mode: [/bold magenta]", end="")

modo = input()

if modo == '1':
    webhook = input("Discord Webhook: ")
    try:
        r = requests.get(webhook)
        r.raise_for_status() 
    except requests.exceptions.HTTPError as e:
        # CAMBIO ADICIONAL: Mejor manejo de errores HTTP para webhooks
        if r.status_code == 401:
            console.print("Invalid webhook (Status 401: Unauthorized)", style="red")
            time.sleep(2.4)
            exit()
        else:
            console.print(f"Error checking webhook (Status {r.status_code}): {e}", style="red")
            time.sleep(2.4)
            exit()
    except requests.exceptions.RequestException as e:
        console.print(f"Connection error checking webhook: {e}", style="red")
        time.sleep(2.4)
        exit()

elif modo == '2':
    console.print(f"[bold magenta] Token: [/bold magenta]", end="")
    TOKENTELEGRAM = input()

    console.print(f"[bold magenta] ChatID: [/bold magenta]", end="")
    CHAT_IDTELEGRAM = input()

    urlTelegram = f"https://api.telegram.org/bot{TOKENTELEGRAM}/sendMessage"

elif modo == '0':
    pass

else:
    console.print("Error: Invalid mode", style="red")
    time.sleep(2)
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

list_file_name = pathlib.Path(file_path).name

try:
    with open(file_path, 'r', encoding='utf-8') as archivo:
        palabras_a_probar = [line.strip() for line in archivo if line.strip()]
    total_palabras = len(palabras_a_probar)
    print(f"Loaded {total_palabras} words from file: {file_path}")
except FileNotFoundError:
    console.print(f"Error: File not found on path: {file_path}", style="red")
    exit()
except Exception as e:
    console.print(f"Error reading the file: {e}", style="red")
    exit()

# --- Configuración de Discord Rich Presence (DRP) ---
rpc = None
try:
    rpc = Presence(CLIENT_ID)
    rpc.connect()
    start_time = time.time()
    console.print("[bold cyan]Discord Rich Presence connected.[/bold cyan]")
    
    # Botones para Rich Presence
    buttons_rpc = [
        {"label": "Github", "url": "https://github.com/ripsaku/steam-id-checker"},
        {"label": "Steam", "url": "https://steamcommunity.com/profiles/76561198783158798/"}
    ]
except Exception as e:
    console.print(f"[bold yellow]Warning: Could not connect to Discord RPC: {e}[/bold yellow]")
    buttons_rpc = [] # Asegura que esté vacío si RPC falla
# ----------------------------------------------------

results_folder = "Results"
if not os.path.exists(results_folder):
    os.makedirs(results_folder)

now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
output_folder = os.path.join(results_folder, timestamp)
os.makedirs(output_folder)

invalid_file_path = os.path.join(output_folder, "INVALID.txt")
valid_file_path = os.path.join(output_folder, "VALID.txt")

invalid_file = open(invalid_file_path, 'w')
valid_file = open(valid_file_path, 'w')

palabras_checkeadas = 0

# 1. ACTUALIZACIÓN INICIAL DEL RPC (0/XXX)
if rpc:
    try:
        rpc.update(
            state=f"Total checked 0/{total_palabras}",  # Estado inicial
            details=f"Checking {list_file_name}",
            large_image="steam",
            large_text="Using Saku's Steam ID Checker",
            start=start_time,
            buttons=buttons_rpc # Agregamos los botones
        )
    except Exception:
        pass


# --- BUCLE PRINCIPAL DE VERIFICACIÓN ---
for palabra in palabras_a_probar:
    palabras_checkeadas += 1

    # 1. AJUSTE DE PAUSA: Solo entra si NO es el final Y es múltiplo de StopQnt
    if (palabras_checkeadas != total_palabras) and (palabras_checkeadas % StopQnt == 0):
        
        # A. Actualizar RPC justo antes de la pausa (ej: 25/XXX)
        if rpc:
            try:
                rpc.update(
                    state=f"Total checked {palabras_checkeadas}/{total_palabras}", 
                    details=f"Checking {list_file_name}",
                    large_image="steam", 
                    large_text="Using Saku's Steam ID Checker",
                    start=start_time,
                    buttons=buttons_rpc
                )
            except Exception:
                pass
        
        # B. Ejecutar la pausa real
        console.print(f"\n[bold yellow]--- Pausing for {StopTime} seconds ({StopQnt} checks completed) ---[/bold yellow]")
        for i in range(StopTime, 0, -1):
            set_console_title(f"PAUSED: {i}s left | IDs: {palabras_checkeadas}/{total_palabras}")
            time.sleep(1)
        console.print("[bold yellow]--- Resuming check ---[/bold yellow]\n")
            
    # Lógica de verificación de ID (Steam)
    if len(palabra) < 3:
        console.print(f'\r[bold yellow]{palabra}[/bold yellow] IS INVALID (too short)')
        invalid_file.write(palabra + '\n')
        invalid_file.flush()
    elif len(palabra) > 32:
        console.print(f'\r[bold yellow]{palabra}[/bold yellow] IS INVALID (too long)')
        invalid_file.write(palabra + '\n')
        invalid_file.flush()
    else:
        try:
            request = requests.get(f'https://steamcommunity.com/id/{palabra}', timeout=10)
            request.raise_for_status() 
            lxml = bs4.BeautifulSoup(request.content, 'lxml')
            title = lxml.find('title')
            list_title = title.text.split()
            
            if list_title and list_title[-1] == "Error": 
                console.print(f'\r[bold green]{palabra}[/bold green] IS AVAILABLE')
                valid_file.write(palabra + '\n')
                valid_file.flush()
                # Notificaciones
                if modo == '1':
                    requests.post(webhook, data={"content" : f"\🌠 New ID available `{palabra}` \n remember **it can be banned** or **blacklisted.** >.<\n`--------------------------------`"})
                elif modo == '2':
                    try:
                        requests.post(
                            urlTelegram,
                            json={
                                "chat_id": CHAT_IDTELEGRAM,
                                "text": f"🌠 New ID available {palabra} \n remember it can be banned or blacklisted. >.<"
                            }
                        ).raise_for_status()
                    except requests.exceptions.RequestException as e:
                        console.print(f"[bold red]Error sending Telegram message:[/bold red] {e}")
            else:
                console.print(f'\r[bold red]{palabra}[/bold red] IS NOT AVAILABLE')
                invalid_file.write(palabra + '\n')
                invalid_file.flush()
        except requests.exceptions.RequestException as e:
            console.print(f'\r[bold red]Error checking {palabra}: {e}[/bold red] (Skipping)')
            invalid_file.write(f'{palabra} # ERROR\n')
            invalid_file.flush()
            
    progress_text = f"IDs: {palabras_checkeadas}/{total_palabras}"
    set_console_title(progress_text)
    time.sleep(0.1)
# --- FIN DEL BUCLE ---

# --- LIMPIEZA Y CIERRE ---
invalid_file.close()
valid_file.close()

if rpc:
    try:
        # Última actualización al finalizar (siempre, para mostrar FINISHED)
        rpc.update(
            state=f"Total checked {palabras_checkeadas}/{total_palabras} (FINISHED)",
            details=f"Checking {list_file_name}",
            large_image="steam",
            large_text="Using Saku's Steam ID Checker",
            start=start_time,
            buttons=buttons_rpc
        )
        rpc.close()
    except:
        pass

console.print("\n\n\n")
console.print(f'[bold magenta]Finished[/bold magenta]')
console.print("\n\n\n")

#Originally made by github.com/Femboysito and github.com/t2zC
#Remade by github.com/ripsaku