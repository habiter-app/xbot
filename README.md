# xbot

**xbot** (read cross-bot), is a code generation tool to translate your messaging bot code for other messaging platform.
-
Problem: I built my bot in X (e.g. Telegram) and now I want to have it also in Y (Discord) and Z (Slack).
xbot solution: xbot takes your code for X and generates automatically code for Y and Z, afterward you can still test it and edit it as you wish. xbot does only the boilerplate part, is up to you what you do with it.

**Why not having a multiplatform bot?**
There are some solution there around multiplatform bot, but different messaging platform offer different features, e.g. in Telegram you can have rich bot UI and in Discord you can display a "Bot is typing" message. More then that you might want to have different deployment strategies for different bot, so with we don't want to force any opinion around what you do with your code.

## Usage

To generate python code (statically) you can

```bash
xbot my_telegram_bot.py --from python-telegram-bot --to discord.py
```

where `python-telegram-bot` is the wrapper you are using to write your Telegram bot.

The main principle around xbot is **the generated code will always run**, even if to do that we need to deprecate some features in the migration.

## How does it work

xbot is built around the concept that different bot APIs wrappers pretty much works the same way just with different syntax. Here is an example with [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)(A) and [discord.py](https://github.com/Rapptz/discord.py)(B).

```python
# python-telegram-bot, (A)

def add(update, context):
    """Add two numbers together."""
    try:
        message = update.message.text
        _, left, right = message.split(" ")
        result = int(left) + int(right)
        update.message.reply_text(result)
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /add <left> <right>')
```

```python
# discord.py, (B)

@bot.command(name='add')
async def add(ctx):
    """Adds two numbers together."""
    try:
        message = ctx.message.content
        _, left, right = message.split(" ")
        result = int(left) + int(right)
        await ctx.send(result)
    except (IndexError, ValueError):
        await ctx.send('Usage: /add <left> <right>')
```

There is a bunch of differences with the two wrappers, but they practically do the same job.
- (A) is sync, (B) is async
- (A) uses plain handlers, (B) uses decorators
- (A) sends a message with `update.message.reply_text`, (B) with `await ctx.send`

NOTE: we are not using the two wrapper in the most idiomatic way we could, but both exampls are still reasonable real-life working examples.

So how can we effectively translate from (A) to (B)? We can use a [Jinja2 template](https://jinja.palletsprojects.com/en/2.11.x/templates/#call) to generate (B)

```python
# discord.py, (B)
# xbot TEMPLATE

@bot.command(name='{{function_name}}')
async def {{function_name}}(ctx):
    """
    {{function_docstring}}
    """
    {{ body }}
```

This basic template we can easily generate the original (B) code, where in {{body}} we are replacing stuff like `update.message.text` to `ctx.message.content`.

Given that template we just need to parse (A) (we can use it [walking the AST](https://docs.python.org/3/library/ast.html#ast.parse) for example) to get the values like function name, arguments and body and then just pass them to (B).

## Contributing

To add a new translation platform this is the checklist

- add a **TEMPLATE** for you library at `xbot/templates/WRAPPER_NAME/reply.py` (to see the full lists of templates and libraries check `xbot/constants.py`)
- add a **DICTIONARY** in `xbot/parsers/WRAPPER_NAME/dictionary.py` (that maps to the `MetaDictionary` in `xbot/templates.py`)
- [optional] add a **PARSER** if you want to translate from your platform to another platform in `xbot/parsers/WRAPPER_NAME/parser.py`
