from core.ui import clear_screen, show_menu, pause

def about_main():
    clear_screen()
    content = """
[bold cyan]TerminalOS v1.0[/bold cyan]

Created by: [green]Anil Yadav[/green]

A lightweight, terminal-based Operating System simulator 
written entirely in Python, utilizing the [magenta]rich[/magenta] library 
for UI presentation.
"""
    show_menu("About", content)
    pause("\nPress Enter to return to Desktop...")
