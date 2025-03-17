import allure
import pytest
from praktikum.burger import Burger
from conftest import mock_sause, mock_topping, mock_bun
from data import DataIngredient, DataPriceAllBurger


class TestsBurger:
    #Проверка метода для добавления булочки в бургер
    def test_add_bun_success(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    #Проверка метода для добавления ингредиентов в бургер
    @pytest.mark.parametrize('ing, add_ing', [
        [DataIngredient.sause_name, DataIngredient.sause_name],
        [DataIngredient.topping_name, DataIngredient.topping_name]
    ])
    def test_add_ingredients_success(self, ing, add_ing):
        burger = Burger()
        burger.add_ingredient(ing)
        assert burger.ingredients == [add_ing]
        assert len(burger.ingredients) == 1

    #Проверка метода для удаления ингредиентов в бургере
    @pytest.mark.parametrize('ing, del_ing', [
        [DataIngredient.sause_name, DataIngredient.sause_name],
        [DataIngredient.topping_name, DataIngredient.topping_name]
    ])
    def test_remove_ingredient_success(self, ing, del_ing):
        burger = Burger()
        burger.add_ingredient(ing)
        burger.remove_ingredient(0)
        assert del_ing not in burger.ingredients

    #Проверка метода для перемещения ингредиентов в бургере
    def test_move_ingredient_success(self, mock_sause, mock_topping):
        burger = Burger()
        burger.add_ingredient(mock_sause)
        burger.add_ingredient(mock_topping)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_topping
        assert burger.ingredients[1] == mock_sause

    #Проверка метода для расчета стоимости бургера
    def test_get_price_success(self, mock_bun,  mock_sause, mock_topping):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sause)
        burger.add_ingredient(mock_topping)
        assert burger.get_price() == DataPriceAllBurger.price_burger

    #Проверка метода получающего рецепт  и стоимость бургера
    def test_get_receipt_success(self, mock_bun, mock_sause, mock_topping):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sause)
        burger.add_ingredient(mock_topping)
        assert burger.get_receipt() == ( '(==== Чиабатта ====)\n'
                                         '= итальянский Пикадор =\n'
                                         '= сливочный Крем-фрэш =\n'
                                         '(==== Чиабатта ====)\n'
                                         '\n'
                                         f'Price: {burger.get_price()}'
        )







