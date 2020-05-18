"""
Dictionary to map telegram code to MetaDictionary
"""
from xbot.templates import MetaDictionary

library_to_meta = {
    'update.message.text': MetaDictionary.RECEIVED_MESSAGE,
    'update.message.reply_text': MetaDictionary.SEND_MESSAGE,
    'update.message.chat': MetaDictionary.CHAT,
    'update.message.from_user': MetaDictionary.USER_SENDER,
}

meta_to_library = { value: key for key, value 
        in library_to_meta.items() }
