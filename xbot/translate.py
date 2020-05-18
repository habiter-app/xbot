"""core translate logic"""
import logging
from dataclasses import dataclass, asdict
from typing import List

import xbot.constants
import xbot.utils

@dataclass
class FunctionTemplateParams:
    """
    Standardises which paramters need to be passed
    to render a 'function' template
    """
    function_name: str
    function_arguments: List[str]
    body: str 
    reply: str 
    function_docstring: str = ''

def parse_source_code(filename, library=None):
    logging.info("parse_source_code..")
    pass

def generate_destination_code(params, output_file):
    logging.info("generate_destination_code..")

    template = "./xbot/templates/discord.py/reply.py"
    params = FunctionTemplateParams(
            function_name = "add", 
            function_arguments = ["left", "right"],
            function_docstring = 'Adds two numbers together.',
            body = 'result = int(left) + int(right)',
            reply = 'result',
            )

    translated_code = xbot.utils.render_jinja_template(template, asdict(params))

    logging.info("\n\n"+translated_code)
    with open(output_file, "w") as f:
        f.write(translated_code)

def translate(sourcecode_filename, output_file=None):
    """
    """
    logging.info("translate {}..".format(sourcecode_filename))
    params = parse_source_code(sourcecode_filename)

    if output_file is None or output_file == "":
        output_file = xbot.constants.DEFAULT_OUTPUT_FILENAME
    generate_destination_code(params, output_file)
