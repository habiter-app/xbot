"""here is the source (to be translated) code"""
import xbot

@xbot.xfunction
def add(update, context):
    try:
        message = update.message.text
        _, left, right = message.split(" ")
        result = int(left) + int(right)
        update.message.reply_text(result)
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /add <left> <right>')

@xbot.xfunction
def subtract(update, context):
    try:
        message = update.message.text
        _, left, right = message.split(" ")
        result = int(left) - int(right)
        update.message.reply_text(result)
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /subtract <left> <right>')

@xbot.xfunction
def echo(update, context):
    update.message.reply_text(update.message.text)

def echo_dont_translate(update, context):
    update.message.reply_text(update.message.text)
