import jinja2
import os
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
