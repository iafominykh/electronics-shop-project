import pytest
from src.phone import Item
from src.Errorex import InstantiateCSVError


def test_item_py_one():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('../src/itemsФ.csv')


def test_item_py_two():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('src/items_fail.csv')