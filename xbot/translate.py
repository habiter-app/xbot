"""core translate logic"""
import ast
import logging
from  dataclasses import asdict

import xbot.constants
import xbot.utils
import xbot.templates


def parse_source_code(
        filename: str, 
        library=None
        ) -> xbot.templates.FunctionTemplateParams:
    """
    """
    logging.info("parse_source_code..")
    sourcecode = ""
    with open(filename, "r") as f:
        sourcecode = f.read()

    Parser = xbot.utils.get_parser(xbot.constants.LIBRARIES.PYTHON_TELEGRAM_BOT)
    parser = Parser(sourcecode=sourcecode)
    params = parser.get_params()
    return params

def generate_destination_code(
        params: xbot.templates.FunctionTemplateParams, 
        output_file: str,
        output_library: xbot.constants.LIBRARIES
        ):
    """
    """
    logging.info("generate_destination_code..")

    template = xbot.utils.template_filename(
            output_library,
            xbot.constants.TEMPLATES.REPLY
            )
    translated_code = xbot.utils.render_jinja_template(template, asdict(params))

    logging.info("\n\n"+translated_code)
    with open(output_file, "w") as f:
        f.write(translated_code)

def translate(
        sourcecode_filename, 
        input_library=xbot.constants.LIBRARIES.PYTHON_TELEGRAM_BOT,
        output_file=None,
        output_library=xbot.constants.LIBRARIES.DISCORD_PY
        ):
    """
    """
    logging.info("translate {}..".format(sourcecode_filename))
    params = parse_source_code(sourcecode_filename)

    if output_file is None or output_file == "":
        output_file = xbot.constants.DEFAULT_OUTPUT_FILENAME
    generate_destination_code(
            params, 
            output_file,
            output_library
            )
