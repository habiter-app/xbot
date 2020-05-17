"""here is the source (to be translated) code"""

def add(update, context):
    """Add two numbers together."""
    try:
        left, right = int(context.args[0]), int(context.args[1])
        result = left + right
        update.message.reply_text(result)
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /add <left> <right>')
