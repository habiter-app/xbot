import functools

def xfunction(func):
    """
    This is a decorator to add in front of functions
    you want to translate. It doesn't do anything by
    itself but it's used by the parser to figure out
    whether to translate this function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwds):
        return func(*args, **kwds)
    return wrapper

