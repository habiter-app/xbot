"""here is the source (to be translated) code"""

def add(update, context):
    """Add two numbers together."""
    try:
        left, right = int(context.args[0]), int(context.args[1])
        result = left + right
        update.message.reply_text(result)
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /add <left> <right>')

def subtract(update, context):
    """Subtract two numbers together."""
    try:
        left, right = int(context.args[0]), int(context.args[1])
        result = left - right
        update.message.reply_text(result)
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /add <left> <right>')

'''
def echo(update, context):
    """Subtract two numbers together."""
    update.message.reply_text(update.message.text)
'''
