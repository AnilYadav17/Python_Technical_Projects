import time
from functools import reduce
from core.ui import clear_screen, show_menu, show_loading, show_message, pause

def add(args):
    return sum(args)

def sub(args):
    return reduce(lambda x,y:x-y ,args)

def multi(args):
    return reduce(lambda x,y:x*y ,args)

def div(args):
    return reduce(lambda x,y:x/y ,args)

def rem(args):
    return reduce(lambda x,y:x%y ,args)

def load():
    clear_screen()
    show_menu("Calculator", "\n  Initializing Modules...\n")
    show_loading("Initializing Modules...", speed=0.01)

def calc_main():
    load()
    while True:
        clear_screen()
        content = """
  [1] Addition          [2] Subtraction       [3] Multiplication
  [4] Division          [5] Remainder         [6] Expression
  [7] Desktop           [0] Previous Menu
"""
        show_menu("Calculator", content)
        
        try:
            choice = int(input("Choice > "))
        except ValueError:
            show_message("Please enter Valid Number", style="red")
            time.sleep(1)
            continue
            
        clear_screen()
        if choice in [1, 2, 3, 4, 5]:
            try:
                x = list(map(int,input("Enter Digits using spaces: ").split()))
                if not x:
                    raise ValueError
            except ValueError:
                show_message("Invalid input", style="red")
                time.sleep(1)
                continue
                
        match choice:
            case 1:
                show_message(f"Sum : {add(x)}", style="bold green")
                pause()
            case 2:
                show_message(f"Subtraction : {sub(x)}", style="bold green")
                pause()
            case 3:
                show_message(f"Multiplication : {multi(x)}", style="bold green")
                pause()
            case 4:
                show_message(f"Division : {div(x)}", style="bold green")
                pause()
            case 5:
                show_message(f"Remainder : {rem(x)}", style="bold green")
                pause()
            case 6:
                expr = input("Enter Expression: ")
                try:
                    show_message(f"Result : {eval(expr)}", style="bold green")
                except Exception as e:
                    show_message(f"Error : {e}", style="red")
                pause()
            case 7:
                return "DESKTOP"
            case 0:
                break
            case _:
                show_message("Please enter Valid Number", style="red")
                time.sleep(1)