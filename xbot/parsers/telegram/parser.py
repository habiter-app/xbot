import xbot.templates
import ast

class Parser:
    def __init__(self, sourcecode: str):
        self.sourcecode = sourcecode

    def parse(self):
        ast_root = ast.parse(self.sourcecode)
        # TODO
        import pdb;pdb.set_trace()

    def get_params(self) -> xbot.templates.FunctionTemplateParams:
        params = xbot.templates.FunctionTemplateParams(
                function_name = "add", 
                function_arguments = ["left", "right"],
                function_docstring = 'Adds two numbers together.',
                body = 'result = int(left) + int(right)',
                reply = 'result',
                )
        return params
