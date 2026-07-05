from rich.console import Console
from rich.panel import Panel

console = Console()

console.print(
    Panel.fit(
        "[bold cyan]Welcome to Rich Module[/bold cyan]\n"
        "[green]Presentation by Anil Yadav[/green]",
        title="Python Rich",
        border_style="red"
    )
)



from rich.console import Console

console = Console()

console.print("[red]Red Text[/red]")
console.print("[green]Green Text[/green]")
console.print("[yellow]Yellow Text[/yellow]")
console.print("[bold blue]Bold Blue Text[/bold blue]")
console.print("[italic magenta]Italic Magenta[/italic magenta]")
	


from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Programming Languages")

table.add_column("Language", style="cyan")
table.add_column("Difficulty", justify="center")
table.add_column("Popularity", justify="center")

table.add_row("Python", "Easy", "⭐⭐⭐⭐⭐")
table.add_row("Java", "Medium", "⭐⭐⭐⭐")
table.add_row("C++", "Hard", "⭐⭐⭐⭐")

console.print(table)
