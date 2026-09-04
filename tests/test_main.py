from typer.testing import CliRunner
from arch_forge.main import app

runner = CliRunner()

def test_init_command():
    result = runner.invoke(app, ["init", "meu-projeto"])
    assert result.exit_code == 0
    assert "Criando novo projeto 'meu-projeto' com Arch Forge" in result.stdout
    assert "Sucesso" in result.stdout
