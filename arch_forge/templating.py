import os
from jinja2 import Environment, FileSystemLoader

# Define the absolute path to the templates directory
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

def render_template(template_name: str, context: dict) -> str:
    """
    Renderiza um template Jinja2 dado o nome e o contexto.
    """
    template = env.get_template(template_name)
    return template.render(context)
