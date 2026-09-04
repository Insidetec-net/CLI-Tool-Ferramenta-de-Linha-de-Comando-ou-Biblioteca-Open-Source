import typer
from rich.console import Console

from typing_extensions import Annotated

app = typer.Typer(help="Arch Forge: O gerador definitivo de microsserviços em Python.")
console = Console()

@app.command()
def init(project_name: Annotated[str, typer.Argument(help="Nome do projeto a ser gerado")]):
    """
    Inicializa um novo projeto com a Arquitetura Hexagonal (DDD).
    """
    console.print(f"[bold green]Criando novo projeto '{project_name}' com Arch Forge...[/bold green]")
    # TODO: Lógica real de cópia dos templates Jinja2

@app.command()
def add(recurso: str):
    """
    Adiciona um novo recurso (ex: endpoint)
    """
    console.print(f"[bold blue]Adicionando {recurso}...[/bold blue]")

if __name__ == "__main__":
    app()
