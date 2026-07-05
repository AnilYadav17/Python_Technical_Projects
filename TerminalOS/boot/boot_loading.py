import time
import os
from rich import print
from core.ui import clear_screen, show_title, show_loading, show_message

LOGGED_IN = False
def clear():
    clear_screen()

def load():
    clear_screen()
    show_title("TerminalOS v1.0")
    print()
    show_loading("Loading...", speed=0.02)
    
def security():
    clear_screen()
    show_title("TerminalOS v1.0")
    global LOGGED_IN
    username = "anil"
    password = "1234"
    attempts=3
    while attempts>0:
        print()
        u_name = input("Enter Username: ")
        u_pass = input("Enter Password: ")
        if u_name == username and u_pass == password:
            LOGGED_IN = True
            clear_screen()
            time.sleep(0.5)
            show_message("Successfully logged in...", style="bold green")
            time.sleep(2)
            clear_screen()
            time.sleep(0.5)
            clear_screen()
            break
        else:
            show_message(f"\nInvalid Username or Password! {attempts-1} Attempts left", style="bold red")
            attempts-=1
            time.sleep(1.5)
            clear_screen()
            show_title("TerminalOS v1.0")
            
    if attempts==0:
        show_message("Too many failed attempts!", style="bold red")
        show_message("Exiting...", style="bold red")
