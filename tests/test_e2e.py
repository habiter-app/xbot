"""e2e translation test"""
import xbot.__main__

def test_e2e__telegram_to_discord():
    sourcecode_filename = "./tests/source.py"
    xbot.__main__.parse_source_code(sourcecode_filename)
