import pytest
from ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price', [
        ('FILLING', 'cheese', 60),
        ('SAUCE', 'barbecue', 40)
    ])
    def test_create_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.name == name
        assert ingredient.price == price
        assert  ingredient.type == ingredient_type


    @pytest.mark.parametrize('ingredient_type, name, price', [
        ('FILLING', 'cheese', 0),
        ('SAUCE', 'barbecue', 42.9),
        ('FILLING', 'meat', 190)
    ])
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price


    @pytest.mark.parametrize('ingredient_type, name, price', [
        ('FILLING', 'cheese', 0),
        ('FILLING', 'МЯСО', 190)
    ])
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name


    @pytest.mark.parametrize('ingredient_type, name, price', [
        ('FILLING', 'cheese', 0),
        ('SAUCE', 'barbecue', 42.9),
    ])
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
