from typer.testing import CliRunner
from arch_forge.main import app

runner = CliRunner()
result = runner.invoke(app, ["init", "meu-projeto"])
print(result.exit_code)
print(result.output)
if result.exception:
    print(result.exception)
