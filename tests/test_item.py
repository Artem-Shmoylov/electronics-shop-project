"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def test_item():
    return Item("Телевизор", 600000, 14)

@pytest.fixture
def test_item2():
    return Phone("Смартфон", 15000, 15, 2)



def test_init(test_item):
    assert test_item.name == "Телевизор"
    assert test_item.price == 600000
    assert test_item.quantity == 14


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 8400000


def test_apply_discount(test_item):
    test_item.apply_discount()
    assert test_item.price == 600000.0
    test_item.pay_rate = 0.5
    test_item.apply_discount()
    assert test_item.price == 300000.0


def test_name_setter(test_item):
    test_item.name = 'Экран'
    assert test_item.name == "Экран"
    with pytest.raises(Exception):
        test_item.name = "Микроволновка"


def test_instantiate_from_csv(test_item):
    assert Item.instantiate_from_csv() is None


def test_string_to_number():
    assert Item.string_to_number("6.5") == 6
    assert Item.string_to_number(6.5) == 6
    with pytest.raises(ValueError):
        Item.string_to_number("пять")


def test_repr_method(test_item):
    assert repr(test_item) == "Item('Телевизор', 600000, 14)"

def test_str_method(test_item):
    assert str(test_item) == 'Телевизор'

def test_add_method(test_item, test_item2):
    assert test_item + test_item2 == 29
    assert test_item + 10 == None
