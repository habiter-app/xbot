"""
Logic surrounding templates manipulation
"""
from dataclasses import dataclass, asdict
from typing import List

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
