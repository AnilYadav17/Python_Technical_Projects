import subprocess
from rich import print
from core.ui import clear_screen, show_title, show_message

def terminal_main():
    clear_screen()
    show_title("Mini Terminal")
    show_message("Type 'exit' to return to Desktop\n", style="green")
    
    while True:
        cmd = input("TerminalOS:~ $ ")
        if cmd.strip().lower() == "exit":
            break
        elif cmd.strip():
            try:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                if result.stdout:
                    print(result.stdout)
                if result.stderr:
                    show_message(result.stderr, style="red")
            except Exception as e:
                show_message(f"Error: {e}", style="red")
