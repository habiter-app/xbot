"""e2e translation test"""
import asyncio
import pytest

import xbot
import xbot.__main__
import xbot.constants

def test_e2e__telegram_to_discord():
    sourcecode_filename = "./tests/original_code.py"
    xbot.translate.translate(sourcecode_filename)

    expected_code = ""
    with open("./tests/translated_code__expected.py","r") as f:
        expected_code = f.read()

    translated_code = ""
    with open(xbot.constants.DEFAULT_OUTPUT_FILENAME, "r") as f:
        translated_code = f.read()

    assert expected_code == translated_code

@xbot.xfunction
def example_function(a):
    return a + 1

@xbot.xfunction
async def example_async_function(a):
    await asyncio.sleep(1)
    return a + 1

@pytest.mark.asyncio
async def test__xfunction():
    """
    we just want to test that the decorator
    compiles and doesn't break anything
    since is used only for parsing
    """
    assert example_function(1) == 2
    assert asyncio.iscoroutinefunction(example_async_function)
    temp = await example_async_function(1)
    assert temp == 2
