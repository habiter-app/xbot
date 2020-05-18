@bot.command(name='add')
async def add(ctx):
    """__GENERATED__ cross platform generated function"""
    try:
        message = ctx.message.content
        (_, left, right) = message.split(' ')
        result = (int(left) + int(right))
        await ctx.send(result)
    except (IndexError, ValueError):
        await ctx.send('Usage: /add <left> <right>')

@bot.command(name='subtract')
async def subtract(ctx):
    """__GENERATED__ cross platform generated function"""
    try:
        message = ctx.message.content
        (_, left, right) = message.split(' ')
        result = (int(left) - int(right))
        await ctx.send(result)
    except (IndexError, ValueError):
        await ctx.send('Usage: /subtract <left> <right>')

@bot.command(name='echo')
async def echo(ctx):
    """__GENERATED__ cross platform generated function"""
    await ctx.send(ctx.message.content)