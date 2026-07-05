import time
from core.ui import clear_screen, show_menu, show_loading, show_message, pause

def load():
    clear_screen()
    show_menu("Convertor", "\n  Initializing Modules...\n")
    show_loading("Initializing Modules...", speed=0.01)

def convertor_main():
    load()
    while True:
        clear_screen()
        content = """
  [1] Length            [2] Weight            [3] Temperature
  [4] Desktop           [0] Previous Menu
"""
        show_menu("Convertor", content)
        
        try:
            choice = int(input("Choice > "))
        except ValueError:
            show_message("Please enter Valid Number", style="red")
            time.sleep(1)
            continue
            
        clear_screen()
        match choice:
            case 1:
                try:
                    cm = float(input("Enter Length in cm: "))
                    show_message(f"Length in inches : {cm / 2.54:.2f}", style="bold green")
                except ValueError:
                    show_message("Invalid input", style="red")
                pause()
            case 2:
                try:
                    kg = float(input("Enter Weight in kg: "))
                    show_message(f"Weight in lbs : {kg * 2.20462:.2f}", style="bold green")
                except ValueError:
                    show_message("Invalid input", style="red")
                pause()
            case 3:
                try:
                    c = float(input("Enter Temperature in Celsius: "))
                    show_message(f"Temperature in Fahrenheit : {(c * 9/5) + 32:.2f}", style="bold green")
                except ValueError:
                    show_message("Invalid input", style="red")
                pause()
            case 4:
                return "DESKTOP"
            case 0:
                break
            case _:
                show_message("Please enter Valid Number", style="red")
                time.sleep(1)
