# Arch Forge CLI

[![CI](https://github.com/Insidetec-net/CLI-Tool-Ferramenta-de-Linha-de-Comando-ou-Biblioteca-Open-Source/actions/workflows/ci.yml/badge.svg)](https://github.com/Insidetec-net/CLI-Tool-Ferramenta-de-Linha-de-Comando-ou-Biblioteca-Open-Source/actions/workflows/ci.yml)

**Arch Forge** é um gerador de projetos (Scaffolder) de linha de comando para aplicações backend em Python. Ele automatiza a criação de microsserviços baseados em **FastAPI** seguindo os princípios de Arquitetura Hexagonal (DDD) e melhores práticas de infraestrutura.

## Funcionalidades
- **Geração de boilerplate imediata**: Templates prontos (Jinja2) de `main.py`, `Dockerfile` e `docker-compose.yml`.
- **Interface Rica**: Desenvolvido com [Typer](https://typer.tiangolo.com/) e [Rich](https://rich.readthedocs.io/), com menus interativos, cores e excelente Developer Experience (DX).
- **Extensível**: Facilidade para criar plugins de novos módulos no futuro.

## Instalação (Desenvolvimento)
Para trabalhar no pacote localmente, utilize um ambiente virtual:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Como usar
Após instalado localmente, a CLI fica disponível globalmente no seu ambiente:

```bash
# Para gerar um novo microsserviço
arch-forge init <nome-do-projeto>

# Para ver os comandos disponíveis
arch-forge --help
```
