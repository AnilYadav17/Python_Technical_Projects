from core.ui import clear_screen, show_menu, pause

def help_main():
    clear_screen()
    content = """
[bold]TerminalOS Help Menu[/bold]

[cyan]Applications[/cyan]: Access essential programs like Calculator and Convertor.
[cyan]Games[/cyan]: Play built-in terminal games.
[cyan]Utilities[/cyan]: System tools and managers.
[cyan]Mini Terminal[/cyan]: Run native OS commands directly.
[cyan]Settings[/cyan]: Customize TerminalOS.

Use the number keys to navigate through menus.
"""
    show_menu("Help", content)
    pause("\nPress Enter to return to Desktop...")
