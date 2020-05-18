"""e2e translation test"""
import xbot.__main__
import xbot.constants

def test_e2e__telegram_to_discord():
    sourcecode_filename = "./tests/source.py"
    xbot.translate.translate(sourcecode_filename)

    expected_code = ""
    with open("./tests/destination.py","r") as f:
        expected_code = f.read()

    translated_code = ""
    with open(xbot.constants.DEFAULT_OUTPUT_FILENAME, "r") as f:
        translated_code = f.read()

    assert translated_code in expected_code
