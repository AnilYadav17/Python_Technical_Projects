import time
from core.ui import clear_screen, show_menu, show_loading, show_message, pause

def load():
    clear_screen()
    show_menu("Utilities", "\n  Initializing Modules...\n")
    show_loading("Initializing Modules...", speed=0.01)

def display_utils():
    load()
    while True:
        clear_screen()
        content = """
  [1] Text Editor       [2] File Explorer     [3] Desktop

  More utilities coming soon...
"""
        show_menu("Utilities", content)
        
        try:
            choice = int(input("Choice > "))
        except ValueError:
            show_message("Please enter Valid Choice", style="red")
            time.sleep(1)
            continue
            
        clear_screen()
        match choice:
            case 1:
                show_message("\nText Editor - Feature under construction!", style="yellow")
                pause()
            case 2:
                show_message("\nFile Explorer - Feature under construction!", style="yellow")
                pause()
            case 3:
                return "DESKTOP"
            case _:
                show_message("Please enter Valid Choice", style="red")
                time.sleep(1)
