import pytest

from src.CSV_error import InstantiateCSVError


def test_csv_error():
    with pytest.raises(InstantiateCSVError, match="Файл повреждён"):
        raise InstantiateCSVError

    with pytest.raises(InstantiateCSVError, match="qwerty"):
        raise InstantiateCSVError('qwerty')