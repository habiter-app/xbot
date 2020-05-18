"""here is the source (to be translated) code"""

def add(update, context):
    try:
        message = update.message.text
        _, left, right = message.split(" ")
        result = int(left) + int(right)
        update.message.reply_text(result)
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /add <left> <right>')

def subtract(update, context):
    try:
        message = update.message.text
        _, left, right = message.split(" ")
        result = int(left) - int(right)
        update.message.reply_text(result)
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /subtract <left> <right>')

def echo(update, context):
    update.message.reply_text(update.message.text)
