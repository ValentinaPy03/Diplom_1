import pytest
from bun import Bun


class TestBun:
    @pytest.mark.parametrize('name, price', [('Кунжутная', 20), ('Сырная', 665)])
    def test_creation_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name and bun.price == price

    @pytest.mark.parametrize('name, price', [('Кунжутная', 20), ('Сырная', 665)])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', [('Кунжутная', 1), ('Сырная', 1500.75), ('Белая', 0)])
    def test_get_price_correct_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price



        
