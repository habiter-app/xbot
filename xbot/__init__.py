import functools
import asyncio

def xfunction(func):
    """
    This is a decorator to add in front of functions
    you want to translate. It doesn't do anything by
    itself but it's used by the parser to figure out
    whether to translate this function.

    Need to support both functions and coroutines,
    see https://stackoverflow.com/questions/44169998/
    """
    @functools.wraps(func)
    def wrapper(*args, **kwds):
        return func(*args, **kwds)

    @functools.wraps(func)
    async def async_wrapper(*args, **kwds):
        return (await func(*args, **kwds))

    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    else:
        return wrapper

