# xbot
[![Build Status](https://travis-ci.com/habiter-app/xbot.svg?branch=master)](https://travis-ci.com/habiter-app/xbot)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/x-bot.svg)](https://badge.fury.io/py/x-bot)

**xbot** (read cross-bot), is a code generation tool for translating messaging bots from one platform to another.

```
pip install x-bot
```

## Abstract

**Problem**: I built my bot in X (e.g. Telegram) and now I want to have it also in Y (Discord) and Z (Slack).
**Solution**: xbot takes your code for X and generates automatically code for Y and Z, afterward you can still test it and edit it as you wish. xbot does only the boilerplate part, is up to you what you do with it.

**Why not having a multiplatform bot?**
There are some solution there around multiplatform bot, but different messaging platform offer different features, e.g. in Telegram you can have rich bot UI and in Discord you can display a "Bot is typing" message. More then that you might want to have different deployment strategies for different bot, so with we don't want to force any opinion around what you do with your code.

## Usage

Decorate functions you want to translate with
```python
@xbot.xfunction
def my_telegram_bot_function(telegram_arguments):
```

And then generate translated python code (statically) with
```bash
python -m xbot my_telegram_bot.py --from python-telegram-bot --to discord.py
```
where `python-telegram-bot` is the wrapper you are using to write your Telegram bot, and `discord.py` is the wrapper you are translating to.

You will now will have a generated code file at `gen__xbot.py` with the transated runnable code. You are free to do what you want with it!

## Example

You can see an example of a real translation in the `tests` folder where we translate from an [orginal_code.py](https://github.com/SolbiatiAlessandro/xbot/blob/master/tests/original_code.py) (that runs in Telegram) to an [translated_code__expected.py](https://github.com/SolbiatiAlessandro/xbot/blob/master/tests/translated_code__expected.py) (that runs in Discord).

To view it your self you can just run the tests to assert that the generated code (inside `gen__xbot.py`) is identical to the expected code.


```
python -m pytest tests
```

[![Build Status](https://travis-ci.com/habiter-app/xbot.svg?branch=master)](https://travis-ci.com/habiter-app/xbot) If the button is green, it means the test above is passing.



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
    {{ body.replace('update.message.text', 'ctx.message.content')}}
```

This basic template we can easily generate the original (B) code.

Given that template we just need to parse (A) (we can use it [walking the AST](https://docs.python.org/3/library/ast.html#ast.parse) for example) to get the values like function name, arguments and body and then just pass them to (B).

## Contributing

To add a new translation platform this is the checklist

- add a **TEMPLATE** for you library at `xbot/templates/WRAPPER_NAME/reply.py` (to see the full lists of templates and libraries check `xbot/constants.py`)
- add a **DICTIONARY** in `xbot/parsers/WRAPPER_NAME/dictionary.py` (that maps to the `MetaDictionary` in `xbot/templates.py`)
- [optional] add a **PARSER** if you want to translate from your platform to another platform in `xbot/parsers/WRAPPER_NAME/parser.py`. You can pretty much use all the functions inside `xbot/parsers/telegram/parser.py`
