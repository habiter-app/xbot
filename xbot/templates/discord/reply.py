@xbot.xfunction
@bot.command(name='{{function_name}}')
async def {{function_name}}(ctx{{', '.join([''] + function_additional_args)}}):
    {{ function_body }}
