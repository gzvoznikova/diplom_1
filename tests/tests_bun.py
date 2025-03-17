import allure
from conftest import mock_bun
from data import DataBun


class TestsBun:
    #Проверка метода наименования булочки
    def tests_get_name_bun_success(self, mock_bun):
        assert mock_bun.get_name() == DataBun.bun_name

    #Проверка метода стоимости булочки
    def tests_get_price_bun_success(self, mock_bun):
        assert mock_bun.get_price() == DataBun.bun_price