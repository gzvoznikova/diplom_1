import allure
import pytest
from data import DataBaseIngredientAndBun
from conftest import db

class TestsDatabase:
    #Проверка метода для списка булочек
    @pytest.mark.parametrize('id_bun, name_bun, price_bun', DataBaseIngredientAndBun.database_buns)
    def test_available_buns_success(self, db, id_bun, name_bun, price_bun):
        db_bun = db.available_buns()
        assert db_bun[id_bun].get_name() == name_bun
        assert db_bun[id_bun].get_price() == price_bun

    #Проверка метода для списка ингредиентов
    @pytest.mark.parametrize('id_ing, type_ing, name_ing, price_ing', DataBaseIngredientAndBun.database_ingredients)
    def test_available_ingredients_success(self, db, id_ing, type_ing, name_ing, price_ing):
        db_ingredients = db.available_ingredients()
        assert db_ingredients[id_ing].get_type() == type_ing
        assert db_ingredients[id_ing].get_name() == name_ing
        assert db_ingredients[id_ing].get_price() == price_ing
