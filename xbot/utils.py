import jinja2
import os
import importlib
import xbot.constants

def render_jinja_template(filename: str, args: dict = {}) -> str:
    template = ""
    with open(filename) as f:
        template = f.read()
    jinja_template = jinja2.Template(template)
    translated_code = jinja_template.render(args)
    return translated_code

def template_filename(
        library: xbot.constants.LIBRARIES, 
        template: xbot.constants.TEMPLATES
        ) -> str:
    return os.path.join("xbot", "templates", library.value, template.value)

def get_parser(library: xbot.constants.LIBRARIES):
    """
    return a Parser class for a given library
    """
    parser_path = ".".join(["xbot", "parsers", library.value, "parser"])
    parser_module = importlib.import_module(parser_path, "xbot")
    parser = parser_module.Parser
    return parser
