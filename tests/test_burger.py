from conftest import *

class TestBurger:
    def test_set_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        first_burger = len(burger.ingredients)
        burger.remove_ingredient(0)
        second_burger = len(burger.ingredients)
        assert first_burger - second_burger == 1

    def test_move_ingredient(self, burger, mock_ingredient, mock_new_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_new_ingredient)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_new_ingredient

    def test_get_price(self, burger, mock_ingredient, mock_bun):
        burger.bun = mock_bun
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 29

    def test_get_receipt(self, burger, mock_ingredient, mock_bun):
        burger.bun = mock_bun
        burger.add_ingredient(mock_ingredient)
        expected_receipt = '(==== Cheese ====)\n= filling tomato =\n(==== Cheese ====)\n\nPrice: 29'
        receipt = burger.get_receipt()
        assert receipt == expected_receipt







