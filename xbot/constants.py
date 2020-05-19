import enum
import os
DEFAULT_OUTPUT_FILENAME = "gen__xbot.py"
GENERATED_COMMENT = '"""__GENERATED__ cross platform generated function"""'
XBOT_PATH = absolute_path = os.path.dirname(os.path.abspath(__file__))

class TEMPLATES(enum.Enum):
    """
    These are the supported templates, i.e. the classes
    of function that xbot can generate
    """

    # REPLY is basic get arguments, 
    # process them and send reply template
    REPLY = 'reply.py'

class LIBRARIES(enum.Enum):
    """
    These are the supported messaing platform APIs
    wrapper to translate between
    """

    # https://github.com/Rapptz/discord.py
    DISCORD_PY = 'discord'

    # https://github.com/python-telegram-bot/python-telegram-bot
    PYTHON_TELEGRAM_BOT = 'telegram'
