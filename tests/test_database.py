from conftest import database

class TestDatabase:
    def test_init_database(self, database):
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6

    def test_available_buns(self, database):
        list_bun = database.available_buns()
        assert type(list_bun) == list

    def test_available_ingredients(self, database):
        list_ingredients = database.available_ingredients()
        assert type(list_ingredients) == list