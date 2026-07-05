import time
from applications.calculator import calc_main
from applications.calendar import calendar_main
from applications.convertor import convertor_main
from desktop import desktop_loading
from core.ui import clear_screen, show_menu, show_loading, show_message, pause

def load():
    clear_screen()
    show_menu("Applications", "\n  Initializing Modules...\n")
    show_loading("Initializing Modules...", speed=0.01)

def display_main():
    load()
    while True:
        clear_screen()
        content = """
  [1] Calculator        [2] Calendar          [3] Convertor
  
  [4] Desktop

  More applications coming soon...
"""
        show_menu("Applications", content)
        
        try:
            choice = int(input("Choice > "))
        except ValueError:
            show_message("Please enter Valid Choice", style="red")
            time.sleep(1)
            continue
            
        clear_screen()
        match choice:
            case 1:
                if calc_main() == "DESKTOP":
                    clear_screen()
                    desktop_loading.load()
                    break
            case 2:
                show_menu("Calendar", calendar_main())
                pause()
            case 3:
                if convertor_main() == "DESKTOP":
                    clear_screen()
                    desktop_loading.load()
                    break
            case 4:
                clear_screen()
                desktop_loading.load()
                break
            case _:
                show_message("Please enter Valid Choice", style="red")
                time.sleep(1)