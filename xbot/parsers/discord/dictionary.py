"""
Dictionary to map discord code to MetaDictionary
"""
from xbot.templates import MetaDictionary

library_to_meta = {
    'ctx.message.content': MetaDictionary.RECEIVED_MESSAGE,
    'await ctx.send': MetaDictionary.SEND_MESSAGE
}

meta_to_library = { value: key for key, value 
        in library_to_meta.items() }
