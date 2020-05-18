"""here is the destination (translated) code"""


@bot.command()
async def add(ctx, left, right):
    """Adds two numbers together."""
    result = int(left) + int(right)
    await ctx.send(result)

@bot.command()
async def subtract(ctx, left, right):
    """Adds two numbers together."""
    result = int(left) + int(right)
    await ctx.send(result)
