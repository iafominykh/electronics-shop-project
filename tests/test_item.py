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


def test_string_to_number():
    assert Item.string_to_number("7.77") == 7

def test_name():
    item1 = Item('Microwave', 10000, 1)
    item2 = Item('Refregerator', 5000, 1)
    assert len(item1.name) <= 10
    assert item2.name == 'Refregerator'


def test_str(return_date):
    assert str(return_date) == 'Смартфон'

def test_repr(return_date):
    assert repr(return_date) == "Item('Смартфон', 5000, 20)"

def test_instantiate_from_csv():
    item1 = Item('Смартфон', 10000, 1)
    item1.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'
