from conftest import mock_sause, mock_topping
from data import DataIngredient
import allure

class TestsIngredient:
    #Проверка метода названия соуса
    def tests_get_name_sause_success(self, mock_sause):
        assert mock_sause.get_name() == DataIngredient.sause_name

    #Проверка метода названия начинки
    def tests_get_name_topping_success(self, mock_topping):
        assert mock_topping.get_name() == DataIngredient.topping_name

    #Проверка метода типа соуса
    def tests_get_type_sause(self, mock_sause):
        assert mock_sause.get_type() == DataIngredient.sause_type

    #Проверка метода типа начинки
    def tests_get_type_topping(self, mock_topping):
        assert mock_topping.get_type() == DataIngredient.topping_type

    #Проверка метода стоимости соуса
    def tests_get_price_sause(self, mock_sause):
        assert mock_sause.get_price() == DataIngredient.sause_price

    #Проверка метода стоимости начинки
    def tests_get_price_toppnig(self, mock_topping):
        assert mock_topping.get_price() == DataIngredient.topping_price