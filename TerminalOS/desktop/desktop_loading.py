import datetime
from core.ui import show_menu

def load():
    x = datetime.datetime.now().date()
    y = datetime.datetime.now().time().strftime("%H:%M:%S")
    content = f"""
[cyan]User[/cyan]    : [green]Anil[/green]
[cyan]Date[/cyan]    : {x}
[cyan]Time[/cyan]    : {y}
[cyan]Status[/cyan]  : [bold green]● Online[/bold green]

------------------------------------------------------------------

  [1] Applications      [2] Games         [3] Utilities
  [4] Mini Terminal     [5] Settings      [6] Help
  [7] Calculator        [8] About
  
  [9] Logout            [0] Shutdown
"""
    show_menu("TerminalOS Desktop", content)
