"""
Logic surrounding templates manipulation
"""
from dataclasses import dataclass, asdict, field
from typing import Iterator, List
import enum

@dataclass
class FunctionTemplateParams:
    """
    Standardises which paramters need to be passed
    to render a 'function'template
    """
    function_name: str
    function_body: str 

    # functions usually have "bot context" arguments like
    # context, update, or ctx. We support additional custom arguments
    # usually for helper functions in the translation
    function_additional_args: List[str]

class MetaDictionary(enum.Enum):
    """
    this are the keywork that we map every
    wrapper to for translationj
    """
    RECEIVED_MESSAGE = 'input message string for the bot function'
    SEND_MESSAGE = 'method to send a message as reply'
    CHAT = 'chat object'
    USER_SENDER = 'user object who sent the message'
