import pytest

from src.phone import Phone


@pytest.fixture
def return_date():
    """Описание фикстуры для тестов"""
    return Phone("Смартфон", 10000, 20, 1)



def test_repr(return_date):
    """Тест для метода repr"""
    assert repr(return_date) == "Phone('Смартфон', 10000, 20, 1)"
