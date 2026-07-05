import os
import time
from rich import print
from rich.panel import Panel
from rich.progress import track
from rich.align import Align

PANEL_WIDTH = 70

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def show_title(title):
    print(Panel(
        Align.center(f"[bold cyan]{title}[/bold cyan]"),
        width=PANEL_WIDTH,
        border_style="blue"
    ))

def show_menu(title, content):
    print(Panel(
        content,
        title=f"[bold cyan]{title}[/bold cyan]",
        width=PANEL_WIDTH,
        border_style="blue"
    ))

def show_loading(text="Loading...", speed=0.01):
    for _ in track(range(100), description=f"[green]{text}[/green]"):
        time.sleep(speed)
    print()

def show_message(text, style="cyan"):
    print(f"[{style}]{text}[/{style}]")

def pause(text="\nPress Enter to continue..."):
    input(text)

def get_input(prompt="Choice > "):
    return input(prompt)
