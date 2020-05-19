import jinja2
import os
import importlib
import logging

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
    return os.path.join(xbot.constants.XBOT_PATH, "templates", library.value, template.value)

def get_parser(library: xbot.constants.LIBRARIES):
    """
    return a Parser class for a given library
    """
    logging.info("get_parser..")
    parser_path = ".".join(["xbot", "parsers", library.value, "parser"])
    parser_module = importlib.import_module(parser_path, "xbot")

    parser = parser_module.Parser
    logging.info(parser)
    return parser

def make_dictionary(
        from_library: xbot.constants.LIBRARIES,
        to_library: xbot.constants.LIBRARIES
        ):
    """
    uses MetaDictionary to dinamically construct a 1:1 
    mapping for the two libraries
    """
    logging.info("make_dictionary..")
    from_library_path = ".".join(
            ["xbot", "parsers", from_library.value, "dictionary"])
    from_library_module = importlib.import_module(from_library_path, "xbot")
    from_library_to_meta = from_library_module.library_to_meta

    to_library_path = ".".join(
            ["xbot", "parsers", to_library.value, "dictionary"])
    to_library_module = importlib.import_module(to_library_path, "xbot")
    meta_to_library = to_library_module.meta_to_library

    from_library_to_library = {
            from_library_key: meta_to_library[meta_key]
            for from_library_key, meta_key in from_library_to_meta.items()
            }

    logging.info(from_library_to_library)
    return from_library_to_library

