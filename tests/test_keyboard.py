import pytest
from src.keyboard import KeyBoard


@pytest.fixture
def xbox():
    return KeyBoard("xbox", 50000, 5)


def test_init(xbox):
    assert str(xbox) == "xbox"


def test_lang(xbox):
    assert xbox.language == "EN"


def test_change_lang(xbox):
    xbox.change_lang()
    assert xbox.language == "RU"
    xbox.change_lang()
    assert xbox.language == "EN"
