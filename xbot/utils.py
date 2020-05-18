import jinja2

def render_jinja_template(filename: str, args: dict = {}) -> str:
    template = ""
    with open(filename) as f:
        template = f.read()
    jinja_template = jinja2.Template(template)
    translated_code = jinja_template.render(args)
    return translated_code
