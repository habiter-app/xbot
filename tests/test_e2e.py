"""e2e translation test"""
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

def test__xfunction():
    """
    we just want to test that the decorator
    compiles and doesn't break anything
    since is used only for parsing
    """
    assert 2 == example_function(1)
