@xbot.xfunction
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

@xbot.xfunction
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

@xbot.xfunction
@bot.command(name='echo')
async def echo(ctx):
    """__GENERATED__ cross platform generated function"""
    await ctx.send(ctx.message.content)

@xbot.xfunction
@bot.command(name='echo_additional_arguments')
async def echo_additional_arguments(ctx, custom_argument_1, custom_argument_2):
    """__GENERATED__ cross platform generated function"""
    await ctx.send(ctx.message.content)