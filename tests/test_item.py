"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def return_date():
    return Item("Смартфон", 5000, 20)


def test_calculate_total_price(return_date):
    assert return_date.calculate_total_price() == 100000


def test_apply_discount(return_date):
    return_date.pay_rate = 0.7
    return_date.apply_discount()
    assert return_date.price == 3500
