import time
from core.ui import clear_screen, show_menu, show_loading, show_message, pause

def load():
    clear_screen()
    show_menu("Settings", "\n  Initializing Modules...\n")
    show_loading("Initializing Modules...", speed=0.01)
    
def settings_main():
    load()
    while True:
        clear_screen()
        content = """
  [1] Change Theme      [2] Change Username   [3] Desktop
"""
        show_menu("Settings", content)
        
        try:
            choice = int(input("Choice > "))
        except ValueError:
            show_message("Please enter Valid Choice", style="red")
            time.sleep(1)
            continue
            
        clear_screen()
        match choice:
            case 1:
                show_message("\nTheme Settings - Feature under construction!", style="yellow")
                pause()
            case 2:
                show_message("\nUser Settings - Feature under construction!", style="yellow")
                pause()
            case 3:
                return "DESKTOP"
            case _:
                show_message("Please enter Valid Choice", style="red")
                time.sleep(1)
