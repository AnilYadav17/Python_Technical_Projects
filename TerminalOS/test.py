from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.progress import track


print(Panel.fit("[bold cyan]TerminalOS v1.0[/bold cyan]",  padding=(0,25) ,border_style="blue"))

c = Console()

c.print(Panel("Welcome to Home", title="Home"))