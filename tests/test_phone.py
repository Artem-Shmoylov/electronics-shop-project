import pytest

from src.phone import Phone


@pytest.fixture
def test_phone():
    return Phone("Смартфон", 15000, 15, 2)
def test_init(test_phone):
    assert test_phone.name == "Смартфон"
    assert test_phone.price == 15000
    assert test_phone.quantity == 15
    assert test_phone.number_of_sim == 2

def test_repr_method(test_phone):
    assert repr(test_phone) == "Phone('Смартфон', 15000, 15, 2)"

def test_setter_method(test_phone):
    with pytest.raises(ValueError):
        test_phone.number_of_sim = 0


