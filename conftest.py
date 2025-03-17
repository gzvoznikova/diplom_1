import pytest
from praktikum.database import Database
from data import *
from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    mock_for_bun = Mock()
    mock_for_bun.get_name.return_value = DataBun.bun_name
    mock_for_bun.get_price.return_value = DataBun.bun_price
    return mock_for_bun

@pytest.fixture
def mock_sause():
    mock_for_sause = Mock()
    mock_for_sause.get_name.return_value = DataIngredient.sause_name
    mock_for_sause.get_type.return_value = DataIngredient.sause_type
    mock_for_sause.get_price.return_value = DataIngredient.sause_price
    return mock_for_sause

@pytest.fixture
def mock_topping():
    mock_for_topping= Mock()
    mock_for_topping.get_name.return_value = DataIngredient.topping_name
    mock_for_topping.get_type.return_value = DataIngredient.topping_type
    mock_for_topping.get_price.return_value = DataIngredient.topping_price
    return mock_for_topping

@pytest.fixture
def db():
    return Database()

