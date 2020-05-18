import xbot.templates
import xbot.constants
import logging
from typing import Iterator
import ast
import astunparse

class Parser:
    """
    The python-telegram-bot API source code must follow
    this guidelines

    - all module level handlers
    - all the telegram code used must be in the dictionary provided

    You can easily construct any language to language dictionary
    using MetaDictionary
    """
    def __init__(
            self, 
            sourcecode: str, 
            dictionary: dict,
            output_indentation_level: int = 1,
            output_indentation_string: str = "    "
            ):
        self.sourcecode = sourcecode
        self.dictionary = dictionary
        self.indentation_level = output_indentation_level
        self.indentation_string = output_indentation_string
        self.parse()

    def _get_bot_functions(self, ast_module: ast.Module):
        """returns functions from the first level of the AST"""
        module_level_functions = filter(
                lambda node: type(node) == ast.FunctionDef, ast_module.body)

        decorator_list = lambda ast_function: \
            ast_function.decorator_list \
            if 'decorator_list' in ast_function._fields else []

        has_xbot_decorator = lambda ast_function: \
                any(map(lambda ast_decorator: ast_decorator.value.id == 'xbot', 
                    decorator_list(ast_function)))

        xbot_decorated_functions = filter(has_xbot_decorator, module_level_functions)
        return xbot_decorated_functions

    def _translate_line(self, original_line: str) -> str:
        """replace tokens from self.dictionary when found"""
        translated_line = original_line
        for original_token, translated_token in self.dictionary.items():
            translated_line = translated_line\
                    .replace(original_token, translated_token)
        # indent code at every \n
        translated_line = translated_line[:-1].replace( 
                "\n", "\n"+self.indentation_level * self.indentation_string)
        return translated_line

    def _get_function_body(self, ast_function: ast.FunctionDef)  -> str:
        """proceding line by line, unparse the function body and translates it"""
        original_code = map(lambda node: astunparse.unparse(node), ast_function.body)
        translated_code = map(lambda line: self._translate_line(line), original_code)
        return xbot.constants.GENERATED_COMMENT + "\n".join(translated_code)

    def _get_function_params(self, ast_function: ast.FunctionDef)  -> xbot.templates.FunctionTemplateParams:
        """extracts FunctionTemplateParams for an ast.FunctionDef"""
        return xbot.templates.FunctionTemplateParams(
                function_name = ast_function.name,
                function_body = self._get_function_body(ast_function)
                )

    def parse(self) -> Iterator[xbot.templates.FunctionTemplateParams]:
        ast_root = ast.parse(self.sourcecode)
        functions = self._get_bot_functions(ast_root)
        return map(self._get_function_params, functions)

