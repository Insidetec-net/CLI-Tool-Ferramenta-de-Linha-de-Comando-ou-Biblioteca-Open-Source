import os
import typer
from rich.console import Console
from rich.panel import Panel
from typing_extensions import Annotated
from arch_forge.templating import render_template

app = typer.Typer(help="Arch Forge: O gerador definitivo de microsserviços em Python.")
console = Console()

def create_file(path: str, content: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

@app.command()
def init(project_name: Annotated[str, typer.Argument(help="Nome do projeto a ser gerado")]):
    """
    Inicializa um novo projeto com a Arquitetura Hexagonal (DDD).
    """
    console.print(Panel.fit(f"[bold green]Criando novo projeto '{project_name}' com Arch Forge 🚀[/bold green]"))
    
    context = {"project_name": project_name}
    
    # Render and create files
    files = {
        f"{project_name}/src/main.py": "main.py.jinja",
        f"{project_name}/docker-compose.yml": "docker-compose.yml.jinja",
        f"{project_name}/requirements.txt": "requirements.txt.jinja",
        f"{project_name}/README.md": "README.md.jinja",
        f"{project_name}/Dockerfile": "Dockerfile.jinja",
    }
    
    for dest_path, template_name in files.items():
        content = render_template(template_name, context)
        create_file(dest_path, content)
        console.print(f"✅ Criado: [cyan]{dest_path}[/cyan]")
        
    console.print(f"\n[bold green]Sucesso! Projeto '{project_name}' gerado.[/bold green]")
    console.print(f"Execute: [yellow]cd {project_name} && docker-compose up -d --build[/yellow]")

@app.command()
def add(recurso: str):
    """
    Adiciona um novo recurso (ex: endpoint)
    """
    console.print(f"[bold blue]Adicionando '{recurso}' ao projeto atual...[/bold blue]")
    console.print("⚠️ Esta funcionalidade será implementada em futuras versões.")

if __name__ == "__main__":
    app()
