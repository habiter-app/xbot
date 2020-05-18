@bot.command()
async def {{function_name}}(ctx, {{", ".join(function_arguments)}}):
    """{{function_docstring}}"""
    {{ body }}
    await ctx.send({{ reply }})
