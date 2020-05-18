import xbot.templates
from typing import Iterator
import ast

class Parser:
    """
    The python-telegram-bot API source code must follow
    this guidelines

    - all module level handlers
    - in case function needs input arguments, they are wrapped around try except
    and arguments are parsed with context.arg
    """
    def __init__(self, sourcecode: str):
        self.sourcecode = sourcecode
        self.parse()

    def _get_bot_functions(self, ast_module: ast.Module):
        """
        returns functions from the first level of the AST
        """
        return filter(lambda node: type(node) == ast.FunctionDef, ast_module.body)

    def _get_function_params(self, ast_function: ast.FunctionDef)  -> xbot.templates.FunctionTemplateParams:
        params = xbot.templates.FunctionTemplateParams(
                function_name = ast_function.name,
                function_arguments = ["left", "right"],
                function_docstring = 'Adds two numbers together.',
                body = 'result = int(left) + int(right)',
                reply = 'result',
                )
        return params

    def parse(self) -> Iterator[xbot.templates.FunctionTemplateParams]:
        ast_root = ast.parse(self.sourcecode)
        functions = self._get_bot_functions(ast_root)
        return map(self._get_function_params, functions)

