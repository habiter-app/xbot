# xbot

**xbot** (read cross-bot), is a code generation tool to translate your messaging bot code for other messaging platform.

Problem: I built my bot in X (e.g. Telegram) and now I want to have it also in Y (Discord) and Z (Slack).
xbot solution: xbot takes your code for X and generates automatically code for Y and Z, afterward you can still test it and edit it as you wish. xbot does only the boilerplate part, is up to you what you do with it.

**Why not having a multiplatform bot?**
There are some solution there around multiplatform bot, but different messaging platform offer different features, e.g. in Telegram you can have rich bot UI and in Discord you can display a "Bot is typing" message. More then that you might want to have different deployment strategies for different bot, so with we don't want to force any opinion around what you do with your code.

## Usage

To generate python code (statically) you can

```
xbot my_telegram_bot.py --from python-telegram-bot --to discord.py
```

where `python-telegram-bot` is the wrapper you are using to write your Telegram bot.

The main principle around xbot is **the generated code will always run**, even if to do that we need to deprecate some features in the migration.

## How does it work

xbot is built around the concept that different bot APIs wrappers pretty much works the same way just with different syntax. Here is an example with [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)(A) and [discord.py](https://github.com/Rapptz/discord.py)(B).

```
# python-telegram-bot, (A)

def add(update, context):
    """Add two numbers together."""
    try:
        left, right = int(context.args[0]), int(context.args[1])
        result = left + right
        update.message.reply_text(result)
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /add <left> <right>')
```

```
# discord.py, (B)

@bot.command()
async def add(ctx, left, right):
    """Adds two numbers together."""
    result = int(left) + int(right)
    await ctx.send(result)
```

There is a bunch of differences with the two wrappers, but they practically do the same job.
- (A) is sync, (B) is async
- (A) parse arguments, (B) have them in the function signature
- (A) uses plain handlers, (B) uses decorators
- (A) sends a message with `update.message.reply_text`, (B) with `await ctx.send`

So how can we effectively translate from (A) to (B)? We can use a [Jinja2 template](https://jinja.palletsprojects.com/en/2.11.x/templates/#call) to generate (B)

```
# discord.py, (B)
# xbot TEMPLATE

{% macro discord_bot_function(name, arguments, reply='result', docstring=None) %}
  @bot.command()
  async def {{name}}(ctx, {{arguments}}:
	  """{{docstring}}"""
	  {{ caller () }}
	  await ctx.send({{ reply }})
{% endmacro %}
```

We this basic template we can generate the original (B) code with just this call
```
# discord.by, (B)
# xbot CALL

{% call discord_bot_function('add', ['left', 'right'], docstring='Adds two numbers together') %}
    result = int(left) + int(right)
{% endcall %}
```

Given that template we just need to parse (A) (we can use it [walking the AST](https://docs.python.org/3/library/ast.html#ast.parse) for example) to get the values like function name, arguments and body and then just pass them to (B).
