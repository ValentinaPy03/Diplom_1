from unittest.mock import Mock
import pytest
from bun import Bun
from burger import Burger
from database import Database
from ingredient import Ingredient

@pytest.fixture(scope='function')
def burger():
    burger = Burger()
    return burger

@pytest.fixture(scope='function')
def database():
    database = Database()
    return database

@pytest.fixture()
def mock_bun():
    mock = Mock(spec=Bun)
    mock.get_price.return_value = 12
    mock.get_name.return_value = 'Cheese'
    return mock

@pytest.fixture()
def mock_ingredient():
    mock = Mock(spec=Ingredient)
    mock.get_price.return_value = 5
    mock.get_name.return_value = 'tomato'
    mock.get_type.return_value = 'FILLING'
    return mock

@pytest.fixture()
def mock_new_ingredient():
    mock = Mock(spec=Ingredient)
    mock.get_price.return_value = 17
    mock.get_name.return_value = 'meat'
    mock.get_type.return_value = 'FILLING'
    return mock