"""
Dictionary to map telegram code to MetaDictionary
"""
from xbot.templates import MetaDictionary

library_to_meta = {
    'update.message.text': MetaDictionary.RECEIVED_MESSAGE,
    'update.message.reply_text': MetaDictionary.SEND_MESSAGE
}

meta_to_library = { value: key for key, value 
        in library_to_meta.items() }
