import pytest

from src.keyboard import KeyBoard


@pytest.fixture
def test_kb():
    return KeyBoard('Dark Project KD87A', 9600, 5)


def test_language(test_kb):
    assert test_kb.language == "EN"


def test_change_language(test_kb):
    assert test_kb.language == "EN"
    test_kb.change_lang()
    assert test_kb.language == "RU"
    test_kb.change_lang().change_lang()
    assert test_kb.language == "RU"

    print(test_kb.language)
    with pytest.raises(AttributeError):
        test_kb.language = "CH"
